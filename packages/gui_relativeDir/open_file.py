# coding=utf-8
from Tkinter import *
import tkFileDialog
import os

'''
这一节介绍几个常见的Tkinter控件，python中叫做widgets。
Button：简单的按钮，用来执行触发操作，如上例；
Canvas：帆布，结构化的图形界面，可以在上面绘制各种图形，进行图形编辑；
Checkbutton：复选框；
Entry：文本编辑区域，类似于MFC中的text field或text box；
Frame：框架，用来包含其他控件，主要用于控制界面布局；
Label：文本或图片显示；
Menu：菜单；
Menubutton：菜单按钮；
Message：显示文本，和Label控件类似，但是Message可以根据文本的长度自动调整显示；
Radiobutton：单选按钮；
Text：格式化文本显示，允许编辑文本的显示风格和属性。
下面举个例子（其中用到了Checkbutton、Radiobutton、Frame、Entry、Label、Message、Text、Button控件）：
'''

class WidgetsDemo:
    def __init__(self):
        # slef.hereFilePath = StringVar()
        window = Tk()  # 创建一个窗口
        window.title("Acquire relative path")  # 设置标题

        frame0 = Frame(window)  # 创建一个框架
        frame0.pack()  # 将框架frame1放置在window中

        label0 = Label(frame0, text="To achieve the relative path")  # 创建标签
        label0.grid(row=1, column=1)
        #
        # self.v1 = IntVar()
        # # 创建一个复选框，如果选中则self.v1为1,否则为0,当点击cbtBold时，触发processCheckbutton函数
        # cbtBold = Checkbutton(frame1, text="Bold", variable=self.v1,
        #                       command=self.processCheckbutton)
        #
        # self.v2 = IntVar()
        # # 创建两个单选按钮，放置在frame1中，按钮文本是分别是Red和Yellow，背景色分别是红色和黄色，
        # # 当rbRed按钮被选中时self.v2为1,当rbYellow按钮被选中时，self.v2为2，按钮被点击时触发processRadiobutto函数
        # rbRed = Radiobutton(frame1, text="Red", bg="red",
        #                     variable=self.v2, value=1,
        #                     command=self.processRadiobutton)
        # rbYellow = Radiobutton(frame1, text="Yellow", bg="yellow",
        #                        variable=self.v2, value=2,
        #                        command=self.processRadiobutton)
        # # grid布局
        # cbtBold.grid(row=1, column=1)
        # rbRed.grid(row=1, column=2)
        # rbYellow.grid(row=1, column=3)

        #---------------------------------------------------------------------------------------------------------------
        frame1 = Frame(window)  # 创建框架frame2
        frame1.pack()  # 将frame2放置在window中

        label = Label(frame1, text="Here: ")  # 创建标签

        self.hereFilePath = StringVar()
        # 创建Entry，内容是与self.name关联
        entryName = Entry(frame1, textvariable=self.hereFilePath)

        # 创建按钮，点击按钮时触发processButton函数
        btGetName = Button(frame1, text="Get Here",
                           command=self.processButton)

        # grid布局
        label.grid(row=1, column=1)
        entryName.grid(row=1, column=2)
        btGetName.grid(row=1, column=3)

        # ---------------------------------------------------------------------------------------------------------------button 2
        frame2 = Frame(window)  # 创建框架frame2
        frame2.pack()  # 将frame2放置在window中

        label2 = Label(frame2, text="Go: ")  # 创建标签

        self.ThereFilePath = StringVar()
        # 创建Entry，内容是与self.name关联
        entryName2 = Entry(frame2, textvariable = self.ThereFilePath)

        # 创建按钮，点击按钮时触发processButton函数
        btGetName2 = Button(frame2, text="Get Go",
                           command=self.processButton2)

        # 创建消息
        # message = Message(frame2, text="It is a widgets demo")

        # grid布局
        label2.grid(row=1, column=1)
        entryName2.grid(row=1, column=2)
        btGetName2.grid(row=1, column=3)
        # message.grid(row=1, column=4)

        # ---------------------------------------------------------------------------------------------------------------Result
        frame3 = Frame(window)  # 创建框架frame2
        frame3.pack()  # 将frame2放置在window中
        # 创建格式化文本，并放置在window中

        label3 = Label(frame3, text="Result")  # 创建标签

        self.Result = StringVar()
        # 创建Entry，内容是与self.name关联
        entryResult = Entry(frame3, textvariable=self.Result)

        label3.grid(row = 1, column = 1)
        entryResult.grid(row=1,column = 2)


        # text = Text(window)
        # text.pack()
        # self.content = StringVar();
        #
        # text.insert(END, self.content.get()) # END 是插入在当前文本的后面
        # text.insert(END, "these carefully designed examples and use them")
        # text.insert(END, "to create your applications.")

        # 监测事件直到window被关闭
        window.mainloop()

    # 复选框点击按钮函数
    def processCheckbutton(self):
        print ("Check button is:"
               + ("checked" if self.v1.get() == 1 else "unchecked"))

    # 单选按钮点击函数
    def processRadiobutton(self):
        print (("Red" if self.v2.get() == 1 else "Yellow")
               + " is selected.")

    # Get Name按钮点击函数
    def processButton(self):
        filenameHere = tkFileDialog.askopenfilename(initialdir="./", title="Select Here file", filetypes=(("markdown files", "*.md"), ("all files", "*.*")))
        print filenameHere

        self.hereFilePath.set(filenameHere)

    # Get Name按钮点击函数
    def processButton2(self):
        filenameThere = tkFileDialog.askopenfilename(initialdir="./", title="Select Here file",
                                                         filetypes=(("all files", "*.*"),) )
        print filenameThere

        self.ThereFilePath.set(filenameThere)
        self.processRelative();

    def processRelative(self):
        here = self.hereFilePath.get();
        there = self.ThereFilePath.get();

        ll = here.split(os.path.sep)
        l2 = there.split(os.path.sep)

        pos = 0;
        for i in range(len(ll)):
            if ll[i] != l2[i]:
                break;
            pos += 1

        back_level = len(ll) - pos - 1;
        back_path = ''
        for i in range(back_level):
            back_path += '..' + os.path.sep;

        enter = l2[pos:len(l2)]
        go_path = ''
        for i in range(len(enter) - 1):
            go_path += enter[i] + os.path.sep

        # add last file name
        go_path += enter[len(enter) - 1]

        relative_path = back_path + go_path

        self.Result.set(relative_path)


WidgetsDemo()
