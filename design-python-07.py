from turtle import *

bgcolor('black')
speed(0)
hideturtle()
hue = 0.0

color = ('red','blue','cyan','orange')

for n in range (6):
    for x in range(9):
        for i in range(2):
            pensize(4)
            circle(90+n*20,90)
            lt(90)
        lt(45)
        # pencolor("orange")
        pencolor(color[n%4])

done()