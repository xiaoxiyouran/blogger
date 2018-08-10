#coding=utf-8

'''
按钮的使用和消息触发

'''
from Tkinter import *

def processOk():
    print ("OK button is clicked.")

def processCancel():
    print ("Cancel button is clicked")

# 创建一个窗口
window = Tk()

# 创建两个按钮
btOk = Button(window,text = "OK", fg = "red", command = processOk)
btCancel = Button(window,text = "cancel", bg = "yellow", command = processCancel)

# 将按钮置在窗口上
btOk.pack()   # 是在父窗口中一行接着一行进行布局
btCancel.pack()

# 创建一个事件循环，监测事件发生，直到窗口关闭
window.mainloop()   # 创建一个事件循环，不停捕捉窗口中的事件



