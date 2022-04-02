#hello everyone , now we want to construct a spiral using turtle library to python
#first we import the library
import turtle

#define some colors
colors = ['red','yellow','green','purple','blue','orange']

#set up the turtle and background color
t = turtle.Pen()
turtle.bgcolor('black')

#now to movements
for x in range(750):#you can choose the number of the iterations
    #set the color
    t.pencolor(colors[x%6])
    #set the width
    t.width (x/100+1)
    #move the turtle
    t.forward(x)
    #rotate the turtle
    t.left(59)