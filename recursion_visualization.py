#use python turtle library

import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle, lineLen-5)
        
        
#run the algorithm
drawSpiral(myTurtle, 50)
myWin.exitonclick() #keep the window on

