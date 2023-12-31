from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *

class mainframe:

    def __init__(self, parent):
        self.output = ScrolledText(parent, width = 100) 
        self.output.grid(column = 1, row = 0)
        #self.output.insert(INSERT, "obama")
        self.output.configure(state ='disabled') 
        
        self.hello_button = Button(parent, text="Send", command=self.send)
        self.hello_button.grid(column=2, row=1)
        
        self.quit_button = Button(parent, text="Disconnect", command=parent.destroy)
        self.quit_button.grid(column=3, row=1)
        
        self.input = Entry(parent, width = 120)
        self.input.grid(column=1, row=1)
        self.label = Label(parent, text="Text box: ")
        self.label.grid(column=0, row=1)

    def send(self):
        #showinfo(message="Hi there "+self.input.get())
        pass

root = Tk()
app = mainframe(root)
root.mainloop()
