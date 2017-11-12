from tkinter import *
import tkinter.messagebox as messagebox


class Appliacation(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.creatWindow()

    def creatWindow(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.button = Button(self, text='Hello', command=self.hello)
        self.button.pack()
    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'hello,{}'.format(name))


app = Appliacation()
app.master.title('hello,world!')
app.mainloop()
