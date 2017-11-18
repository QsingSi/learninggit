import webbrowser
import tkinter
import os
from tkinter import *
import tkinter.messagebox as messagebox
'''
下一步计划,强制关机,以及完善messagebox确定键的操作
了解python程序如何打包成exe程序
'''


class MyWight(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.creatWindow()
        self.pack()

    def creatWindow(self):
        self.urlLable = Label(
            self, text='输入爸爸,否则你的电脑会关机!!!')
        self.urlLable.grid(row=1, column=1, columnspan=3)
        self.url = Entry(self)
        self.url.grid(row=2, column=1, columnspan=3)
        self.url.bind('<Key-Return>', self.openWeb, add='+')
        self.open = Button(self, text='爸爸', bg='red')
        self.open.bind('<Button-1>', self.openWeb, add='+')
        #self.open.bind('<Enter>', self.openWeb, add='+')
        self.open.grid(row=3, column=1, padx=10)
        self.quit = Button(self, text='no', command=self.shutdown)
        self.quit.grid(row=3, column=3)

    def openWeb(self, event):
        # webbrower.open('http://www.baidu.com', new=1)
        ##url = self.url.get() or 'http://www.baidu.com'
        info = self.url.get()
        if info != '爸爸':
            self.shutdown()
        else:
            messagebox.showinfo('好孩子!!!', '你是我的好孩子啊!!!')
        '''
        if self.url.get():
            url = 'http://www.' + url
        webbrowser.open(url=url, new=1)
        '''

    def shutdown(self):
        os.system('shutdown -s')


mw = MyWight()
mw.master.title('搞你')
mw.master.geometry('300x100')
mw.mainloop()
