""" lets see what I build today .... """
# Goal : Building a city scape generator ->

# imports line
import turtle
import random
loadWindow = turtle.Screen()
turtle.colormode(255)
turtle.speed(0)
"""

turtle.forward(1000)
turtle.backward(1000)
turtle.left(90)
turtle.forward(1000)
turtle.exitonclick()
"""
def home():
    turtle.home()
    
def speed(x):
    turtle.speed(x)
    
def right(x):
    turtle.right(x)

def left(x):
    turtle.left(x)

def forward(x):
    turtle.forward(x)

def backward(x):
    turtle.backward(x)

def circle(x):
    turtle.circle(x)

def up():
    turtle.penup()

def down():
    turtle.pendown()

def randomBout():
    a = random.random()
    b = random.random()
    c = 100
    d = b * c
    turtle.forward(d)

def irisCenter():
    for i in range(360):
        forward(100)
        circle(5)
        up()
        forward(50)
        down()
        forward(50)
        circle(10)
        up()
        backward(200)
        down()
        left(1)

" THE GENERATION OF THE IRIS "

#for i in range(360):
speed(0)

def shape():
    up()
    right(90)
    forward(230)
    left(90)
    down()
    for i in range(121):
        forward(4)
        left(.5)
    up()
    home()
    right(90)
    forward(230)
    right(90)
    down()
    for i in range(121):
        forward(4)
        right(.5)
    up()
    home()
    left(90)
    forward(230)
    right(90)
    down()
    for i in range(121):
        forward(4)
        right(.5)
    up()
    home()
    left(90)
    forward(230)
    left(90)
    down()
    for i in range(121):
        forward(4)
        left(.5)
    up()
    home()
    down()

def equi(x):
    right(90)
    up()
    forward(x)
    left(90)
    down()
    circle(x)
    up()
    home()

shape()
for i in range(230):
    if i > 110 and i < 145:
        equi(i)
    if i > 215:
        equi(i)
        
irisCenter()

    
