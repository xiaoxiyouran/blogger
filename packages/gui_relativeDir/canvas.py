# coding=utf-8
from Tkinter import *

'''
Canvas类似于一个画板，可以在上面绘制各种图形和进行图形编辑，Canvas的坐标系不同于turtle的坐标系，它是以canvas的左上角点为原点(0,0)，以右方和下方为x轴正轴和y轴正轴，并以像素为单位；下面介绍几个常用的绘制函数：

create_rectange(x1,y1,x2,y2)：绘制一个矩形，(x1,y1)为矩形左上角点，(x2,y2)为矩形右下角点；

create_oval(x1,y1,x2,y2)：绘制一个椭圆，(x1,y1)和(x2,y2)分别为椭圆外接矩形的左上角点和右下角点；

create_arc(x1,y1,x2,y2,start,extent)：绘制一个弧形， (x1,y1)和(x2,y2)分别为椭圆或圆外接矩形的左上角点和右下角点，start是弧形角度开始点，extent是弧形角度；

create_polygon(x1,y1,x2,y2,x3,y3)：绘制一个多边形，(xi,yi)分别为各顶点坐标；

create_line(x1,y1,x2,y2)：绘制线条，(x1,y1)和(x2,y2)分别为起始点和结束点；

create_text(x,y,text)：绘制字符串在以(x,y)为中心的位置。
'''

'''
对其中出现的一些字段做简要说明：create_rectangle()中的tags表示的是这个图形在canvas中的标识，在后面的canvas.delete()（删除canvas中的图形）中也使用到；create_oval()中的fill表示的是填充颜色；create_arc()中的width表示的是图形线段的宽度；create_line中的arrow="last"表示在线段末尾加箭头，active fill表示若鼠标移动到这条线段上时，线段的颜色会变成蓝色；create_text()中的font是字体。

'''


window = Tk()
canvas = Canvas(window,width=200,height=100,bg="white")
canvas.pack()
canvas.create_rectangle(10,10,190,90,tags="rect")
# canvas.create_oval(10,10,190,90,fill="red",tags="oval")
# canvas.create_arc(10,10,190,90,start=0,extent=90,width=8,fill="red",tags="arc")
# canvas.create_polygon(10,10,190,90,30,50,tags="poly")
# canvas.create_line(10,90,190,10,width=9,arrow="last",activefill="blue",tags="line")
# canvas.create_text(60,40,text="string",font="Times 10 bold underline",tags="string")
# canvas.delete("rect","oval","arc","poly","line","string")
window.mainloop()