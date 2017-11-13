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
        self.__MAXLEN = 1024

    def creatWindow(self):
        messagebox.showinfo(
            'Message', 'initialize succes! start listening:')
        self.listen = Label(self, text='start listen the port {}'.format(9999))
        self.listen.pack()
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.button = Button(self, text='Send', command=self.hello)
        self.button.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        data, addr = self.recieve()
        #messagebox.showinfo('Message', 'hello,{}'.format(name))
        name = name.encode('ascii')
        self.s.sendto(b'%s' % name, addr)
        rec = 'Recieve from %s:%s' % addr + '\t' + \
            'info:{}'.format(data.decode('utf-8'))
        self.listen = Label(self, text=rec)
        self.listen.pack()
        info = 'send {} to address: {}'.format(name.decode('utf-8'), addr)
        self.nameOutput = Label(self, text=info)
        self.nameOutput.pack()

    def set_param(self, port=9999):
        param = (self.__ip, port)
        self.s.bind(param)

    def recieve(self):
        data, addr = self.s.recvfrom(self.__MAXLEN)
        return data, addr


app = Appliacation()
app.set_param()
app.master.title('hello,world!')
app.mainloop()
