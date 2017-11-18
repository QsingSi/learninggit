import webbrowser
import tkinter
from tkinter import *


class MyWight(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.creatWindow()
        self.pack()

    def creatWindow(self):
        self.urlLable = Label(
            self, text='please input the url you want to acess:')
        self.urlLable.pack()
        self.url = Entry(self)
        self.url.pack()
        self.url.bind('<Key-Enter>', self.openWeb, add='+')
        self.open = Button(self, text='open', command=self.openWeb, bg='red')
        #self.open.bind('<Enter>', self.openWeb, add='+')
        self.open.pack()
        self.quit = Button(self, text='quit', command=quit)
        self.quit.pack(side='right')

    def openWeb(self, event):
        # webbrower.open('http://www.baidu.com', new=1)
        url = self.url.get() or 'http://www.baidu.com'
        if self.url.get():
            url = 'http://www.' + url
        webbrowser.open(url=url, new=1)


mw = MyWight()
mw.master.title('open brower')
mw.master.geometry('100x100')
mw.mainloop()
