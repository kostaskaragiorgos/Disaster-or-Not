from tkinter import Tk, Menu
from tkinter import messagebox as msg

class DisasterOrNot():
    def __init__(self,master):
        self.master = master
        self.master.title("Disaster Or Not")
        self.master.geometry("250x200")
        self.master.resizable(False,False)
        
        self.menu = Menu(self.master)
        
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label="Insert a csv file", accelerator='Ctrl+O', command=self.insertcsv)
        self.file_menu.add_command(label="Close file", accelerator="Ctrl+F4", command=self.closefile)
        self.file_menu.add_command(label="Exit",accelerator= 'Alt+F4',command = self.exitmenu)
        self.menu.add_cascade(label = "File",menu=self.file_menu)
        
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
        pass

    def helpmenu(self):
        pass
    
    def aboutmenu(self):
        pass

        

def main():
    root=Tk()
    DisasterOrNot(root)
    root.mainloop()
    
if __name__=='__main__':
    main()