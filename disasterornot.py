from tkinter import Tk, Menu, Label, Text, Button, END, filedialog
from tkinter import messagebox as msg
import pandas as pd


def aboutmenu():
    """ about menu function """
    msg.showinfo("About", "Disaster Or Not \nVersion 1.0")

class DisasterOrNot():
    def __init__(self,master):
        self.master = master
        self.master.title("Disaster Or Not")
        self.master.geometry("300x300")
        self.master.resizable(False,False)
        self.filename = ""
        self.predictions = ""

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

        self.predictbutton =  Button(self.master, text="Predict")
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
        self.show_menu.add_command(label="Predictions")
        self.menu.add_cascade(label="Show", menu=self.show_menu)
        
        self.about_menu = Menu(self.menu,tearoff = 0)
        self.about_menu.add_command(label = "About",accelerator= 'Ctrl+I',command= aboutmenu)
        self.menu.add_cascade(label="About",menu=self.about_menu)
        
        self.help_menu = Menu(self.menu,tearoff = 0)
        self.help_menu.add_command(label = "Help",accelerator = 'Ctrl+F1',command=self.helpmenu)
        self.menu.add_cascade(label="Help",menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        self.master.bind('<Control-o>', lambda event: self.insertcsv())
        self.master.bind('<Control-F4>', lambda event:self.closefile())
        self.master.bind('<Control-s>', lambda event:self.savepredictions())
        self.master.bind('<Alt-s>', lambda event:self.savetoexisted())
        self.master.bind('<Alt-F4>',lambda event: self.exitmenu())
        self.master.bind('<Control-z>', lambda event:self.clearfunction(None))
        self.master.bind('<Alt-z>', lambda event:self.clearfunction('keyword'))
        self.master.bind('<Alt-x>', lambda event:self.clearfunction('location'))
        self.master.bind('<Alt-c>', lambda event:self.clearfunction('text'))
        self.master.bind('<Control-F1>',lambda event: self.helpmenu())
        self.master.bind('<Control-i>',lambda event: aboutmenu())
    

    def savepredictions(self):
        if self.predictions == "":
            msg.showerror("ERROR", "NO PREDICTIONS TO SAVE")
        else:
            pass


    def savetoexisted(self):
        if self.predictions == "":
            msg.showerror("ERROR", "NO PREDICTIONS TO SAVE")
        else:
            existedfile = filedialog.askopenfilename(initialdir="/", title="Select csv file",
                                                       filetypes=(("csv files", "*.csv"),
                                                                  ("all files", "*.*")))
            if ".csv" in existedfile:
                pass
            else:
                msg.showerror("ERROR", "NO CSV IMPORTED")
                
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
            msg.showinfo("SUSSESS", "YOUR CSV FILE HAS SUCCESFULLY CLOSED")

    def predict(self):
        pass

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


    def helpmenu(self):
        pass


        

def main():
    root=Tk()
    DisasterOrNot(root)
    root.mainloop()
    
if __name__=='__main__':
    main()