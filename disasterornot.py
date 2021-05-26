from operator import index
from tkinter import Tk, Menu, Label, Text, Button, END, filedialog
from tkinter import messagebox as msg
from nltk import corpus
import pandas as pd
import numpy as np
import pickle
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

def aboutmenu():
    """ about menu function """
    msg.showinfo("About", "Disaster Or Not \nVersion 1.0")

def helpmenu():
    """ help menu function """
    msg.showinfo("Help", "INSERT A .CSV FILE OR FILL THE TEXT BOXES TO PREDICT IF THE TEXT REFERS TO A DISASTER OR NOT")

def corpusf(dataframe):
    """ function to create the corpus list.
    Args:
        dataframe: the dataframe
    Returns:
        corpus: a list
    """
    corpus = []
    for i in range(0,len(dataframe)):
        text = re.sub(r'^https?:\/\/.*[\r\n]*', '', dataframe['text'][i], flags=re.MULTILINE)
        text = re.sub('[^a-zA-Z]', ' ', dataframe['text'][i])
        text = text.lower()
        text = text.split()
        ps = PorterStemmer()
        all_stopwords = stopwords.words('english')
        all_stopwords.remove('not')
        text = [word for word in text if not word in set(all_stopwords)]
        text = ' '.join(text)
        corpus.append(text)
    return corpus

class DisasterOrNot():
    def __init__(self,master):
        self.master = master
        self.master.title("Disaster Or Not")
        self.master.geometry("300x300")
        self.master.resizable(False,False)
        self.filename = ""
        self.predictions = ""
        self.model = 'models/GaussianNB_model.sav'

        self.keywordleb = Label(self.master, text="Enter the keyword")
        self.keywordleb.pack()

        self.keywordtext = Text(self.master, height=1, width=8)
        self.keywordtext.pack()


        self.locationleb = Label(self.master, text="Enter the location")
        self.locationleb.pack()

        self.locationtext = Text(self.master, height=1, width=8)
        self.locationtext.pack()
        
        self.textleb = Label(self.master, text="Enter the text")
        self.textleb.pack()

        self.texttext = Text(self.master, height=5, width=25)
        self.texttext.pack()

        self.predictbutton =  Button(self.master, text="Predict", command=self.predict)
        self.predictbutton.pack()

        self.clearbutton = Button(self.master, text="Clear", command= lambda: self.clearfunction(None))
        self.clearbutton.pack()
        

        self.menu = Menu(self.master)
        
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label="Insert a csv file", accelerator='Ctrl+O', command=self.insertcsv)
        self.file_menu.add_command(label="Close file", accelerator="Ctrl+F4", command=self.closefile)
        self.file_menu.add_command(label="Save file", accelerator='Ctrl+S', command=self.savepredictions)
        self.file_menu.add_command(label="Save to existed file", accelerator='Alt+S', command=self.savetoexisted)
        self.file_menu.add_command(label="Exit",accelerator= 'Alt+F4',command = self.exitmenu)
        self.menu.add_cascade(label = "File",menu=self.file_menu)

        self.edit_menu = Menu(self.menu, tearoff= 0)
        self.edit_menu.add_command(label="Clear All", accelerator='Ctrl+Z', command= lambda: self.clearfunction(None))
        self.edit_menu.add_command(label="Clear Keyword", accelerator='Alt+Z', command= lambda: self.clearfunction('keyword'))
        self.edit_menu.add_command(label="Clear Location", accelerator='Alt+X', command= lambda: self.clearfunction('location'))
        self.edit_menu.add_command(label="Clear Text", accelerator='Alt+C', command= lambda: self.clearfunction('text'))
        self.menu.add_cascade(label = "Edit", menu=self.edit_menu)

        self.show_menu = Menu(self.menu, tearoff=0)
        self.show_menu.add_command(label="Predictions", accelerator='Ctrl+F5' ,command=self.showpredictions)
        self.menu.add_cascade(label="Show", menu=self.show_menu)
        
        self.about_menu = Menu(self.menu,tearoff = 0)
        self.about_menu.add_command(label = "About",accelerator= 'Ctrl+I',command= aboutmenu)
        self.menu.add_cascade(label="About",menu=self.about_menu)
        
        self.help_menu = Menu(self.menu,tearoff = 0)
        self.help_menu.add_command(label = "Help",accelerator = 'Ctrl+F1',command= helpmenu)
        self.menu.add_cascade(label="Help",menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        self.master.bind('<Control-o>', lambda event: self.insertcsv())
        self.master.bind('<Control-F4>', lambda event:self.closefile())
        self.master.bind('<Control-s>', lambda event:self.savepredictions())
        self.master.bind('<Alt-s>', lambda event:self.savetoexisted())
        self.master.bind('<Alt-F4>',lambda event: self.exitmenu())
        self.master.bind('<Control-F5>', lambda event: self.showpredictions())
        self.master.bind('<Control-z>', lambda event:self.clearfunction(None))
        self.master.bind('<Alt-z>', lambda event:self.clearfunction('keyword'))
        self.master.bind('<Alt-x>', lambda event:self.clearfunction('location'))
        self.master.bind('<Alt-c>', lambda event:self.clearfunction('text'))
        self.master.bind('<Control-F1>',lambda event: helpmenu())
        self.master.bind('<Control-i>',lambda event: aboutmenu())
    

    def showpredictions(self):
        """ shows the predictions to the user"""
        if self.predictions == "":
            msg.showerror("ERROR", "NO PREDICTIONS TO SHOW")
        else:
            msg.showinfo("PREDICTIONS", str(self.predictions))


    def savepredictions(self):
        """ saves the predictions to a new .csv file """
        if self.predictions == "":
            msg.showerror("ERROR", "NO PREDICTIONS TO SAVE")
        else:
            filenamesave = filedialog.asksaveasfilename(initialdir="/", title="Select file",
                                                    filetypes=(("csv files", "*.csv"),
                                                                ("all files", "*.*")))
            self.checktosave(filenamesave)

    def checktosave(self, filename):
        if filename is None or filename == "":
            msg.showerror("ERROR", "NO FILE SAVED")
        else:
            np.savetxt(str(filename)+".csv", self.predictions)
            msg.showinfo("SUCCESS", "CSV FILE SAVED SUCCESSFULLY")

    def savetoexisted(self):
        if self.predictions == "":
            msg.showerror("ERROR", "NO PREDICTIONS TO SAVE")
        else:
            existedfile = filedialog.askopenfilename(initialdir="/", title="Select csv file",
                                                       filetypes=(("csv files", "*.csv"),
                                                                  ("all files", "*.*")))
            if ".csv" in existedfile and self.predictions != "":
                df = pd.read_csv(existedfile)
                df['Predictions'] = self.predictions
                df.to_csv(existedfile+".csv")
            else:
                msg.showerror("ERROR", "NO CSV IMPORTED OR NO PREDICTIONS TO SAVE")
                
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    
    def insertcsv(self):
        if self.filename != "":
            msg.showerror("ERROR", "FILE IS ALREADY OPEN")
        else:
            self.filename = filedialog.askopenfilename(initialdir="/", title="Select csv file",
                                                       filetypes=(("csv files", "*.csv"),
                                                                  ("all files", "*.*")))
            if ".csv" in self.filename:
                self.df = pd.read_csv(self.filename)
                if all([item in self.df.columns for item in ['keyword', 'location', 'text']]):
                    msg.showinfo("SUCCESS", "CSV FILE ADDED SUCCESSFULLY")
                    self.importeddf = pd.read_csv(self.filename)
                    self.statechange("disable")
                else:
                    self.filename = ""
                    msg.showerror("ERROR", "NO PROPER CSV ")
  
            else:
                self.filename = ""
                msg.showerror("ERROR", "NO CSV IMPORTED")

    def closefile(self):
        if self.filename == "":
            msg.showerror("ERROR", "NO FILE TO CLOSE")
        else:
            self.filename = ""
            self.predictions = ""
            self.statechange("normal")
            msg.showinfo("SUSSESS", "YOUR CSV FILE HAS SUCCESFULLY CLOSED")

    def statechange(self, state):
        """ changes the state of buttons, texts etc.. """
        self.keywordtext.config(state=state)
        self.texttext.config(state=state)
        self.locationtext.config(state=state)

    def predict(self):
        if self.filename != "" and self.predictions == "":
            corpus = corpusf(self.importeddf)
            cv = CountVectorizer(max_features=2000)
            X = cv.fit_transform(corpus).toarray()
            loadedmodel = pickle.load(open(self.model, 'rb'))
            self.predictions = loadedmodel.predict(X)
        elif self.predictions != "":
            msg.showinfo("PREDICTIONS", str(self.predictions))


    def clearfunction(self, field):
        if field == "location":
            self.locationtext.delete(1.0, END)
        elif field == "keyword":
            self.keywordtext.delete(1.0, END)
        elif field == "text":
            self.texttext.delete(1.0, END)
        else:
            self.keywordtext.delete(1.0, END)
            self.locationtext.delete(1.0, END)
            self.texttext.delete(1.0, END)



def main():
    root=Tk()
    DisasterOrNot(root)
    root.mainloop()
    
if __name__=='__main__':
    main()