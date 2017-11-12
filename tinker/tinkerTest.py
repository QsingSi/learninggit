from tkinter import *
import tkinter.messagebox as messagebox
import socket


class Appliacation(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.creatWindow()
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__ip = '127.0.0.1'
        self.flag = False
        self.__MAXLEN = 1024

    def creatWindow(self):
        if self.flag == True:
            messagebox.showinfo(
                'Message', 'initialize succes! start listening:')
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.button = Button(self, text='Hello', command=self.hello)
        self.button.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        data, addr = self.recieve()
        #messagebox.showinfo('Message', 'hello,{}'.format(name))
        self.s.sendto(b'hello,%s' % data, addr)
        info = 'send {} to address: {}'.format(name, addr)
        self.nameOutput = Label(self, text=info)
        self.nameOutput.pack()

    def set_param(self, port=9999):
        param = (self.__ip, port)
        self.s.bind(param)
        self.flag = True

    def recieve(self):
        data, addr = self.s.recvfrom(self.__MAXLEN)
        return data, addr


app = Appliacation()
app.master.title('hello,world!')
app.mainloop()
