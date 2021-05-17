from tkinter import Tk, Menu, Label, Text, Button, END
from tkinter import messagebox as msg

class DisasterOrNot():
    def __init__(self,master):
        self.master = master
        self.master.title("Disaster Or Not")
        self.master.geometry("300x300")
        self.master.resizable(False,False)

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

        self.clearbutton = Button(self.master, text="Clear", command=self.clear)
        self.clearbutton.pack()
        

        self.menu = Menu(self.master)
        
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label="Insert a csv file", accelerator='Ctrl+O', command=self.insertcsv)
        self.file_menu.add_command(label="Close file", accelerator="Ctrl+F4", command=self.closefile)
        self.file_menu.add_command(label="Exit",accelerator= 'Alt+F4',command = self.exitmenu)
        self.menu.add_cascade(label = "File",menu=self.file_menu)

        self.edit_menu = Menu(self.menu, tearoff= 0)
        self.edit_menu.add_command(label="Clear", command=self.clear)
        self.menu.add_cascade(label = "Edit", menu=self.edit_menu)
        
        self.about_menu = Menu(self.menu,tearoff = 0)
        self.about_menu.add_command(label = "About",accelerator= 'Ctrl+I',command=self.aboutmenu)
        self.menu.add_cascade(label="About",menu=self.about_menu)
        
        self.help_menu = Menu(self.menu,tearoff = 0)
        self.help_menu.add_command(label = "Help",accelerator = 'Ctrl+F1',command=self.helpmenu)
        self.menu.add_cascade(label="Help",menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        self.master.bind('<Alt-F4>',lambda event: self.exitmenu())
        self.master.bind('<Control-F1>',lambda event: self.helpmenu())
        self.master.bind('<Control-i>',lambda event: self.aboutmenu())

    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    
    def insertcsv(self):
        pass

    def closefile(self):
        pass

    def predict(self):
        pass

    def clear(self):
        self.keywordtext.delete(1.0, END)
        self.locationtext.delete(1.0, END)
        self.texttext.delete(1.0, END)


    def helpmenu(self):
        pass
    
    def aboutmenu(self):
        pass

    def clear(self):
        pass

        

def main():
    root=Tk()
    DisasterOrNot(root)
    root.mainloop()
    
if __name__=='__main__':
    main()