from tkinter import *


class Appliacation(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.creatWindow()

    def creatWindow(self):
        self.helloLabel = Label(self, text='hello,world!')
        self.helloLabel.pack()
        self.button = Button(self, text='Quit', COMMAND=self.creatWindow())
        self.button.pack()


app = Appliacation()
app.master.title('hello,world!')
app.mainloop()
