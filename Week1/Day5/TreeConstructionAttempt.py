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

def direc(x):
    if x > 180:
        y = 360 - x
        right(y)
        
    if x < 180:
        left(x)
        
    if x == 180:
        left(x)
        

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

def circleGap():
    for i in range(230):
        if i > 110 and i < 145:
            equi(i)
        if i > 215:
            equi(i)

def iris():
    shape()
    circleGap()
    irisCenter()
    
def shome(slong = 300, slat = 300):
    home()
    left(180)
    up()
    forward(slong)
    left(90)
    forward(slat)
    left(90)
    down()
    
#so I want to make a curve constructor here... meaning that we generate some form of
    # counter for first second ie extra order curves.
def setGraph(x):
    forward(x)
    shome()
    left(90)
    forward(x)
    shome()

#x the length
#y the concave

def curve(x,y):
    tl = int( (x * (2 ** .5) ) /y)
    print(tl)
    for i in range(tl):
        forward(y)
        direc(.5)
    up()
    shome()
    down()
    
x = 100
#setGraph(x)
#curve(x,4)

#shome()
#for i in range(2,20):
#    curve(x,i)

def Pendulum(i):
    up()
    home()
    right(90)
    forward(i)
    down()
    left(90)
    for i in range(40):
        forward(5)
        left(1)
    for i in range(80):
        forward(-5)
        right(1)
    up()
    for i in range(40):
        forward(5)
        left(1)
    down()

def presentGround(x):
    left(180)
    forward(x)
    shome()
    forward(x)
    up()
    shome()
    down()

def trunkMe():
    up()
    forward(10)
    left(90)
    down()
    forward(60)
    up()
    left(180)
    forward(60)
    right(90)
    forward(10)
    forward(10)
    right(90)
    down()
    forward(60)
    right(90)
def treeFluff():
    forward(40)
    left(90)
    forward(40)
    left(90)
    forward(60)
    left(90)
    forward(40)
    left(90)
    forward(20)
    up()
def treeMe():
    trunkMe()
    treeFluff()
    home()
def precess(x,y):
    shome()
    for i in range(1,y):
        up()
        forward(i*x)
        down()
        treeMe()
        shome()

def a89():
    up()
    down()
    for i in range(500):
        forward(i)
        forward(10)
        left(89)
        
def a90():
    up()
    down()
    for i in range(500):
        forward(i)
        forward(10)
        left(90)

def a91():
    up()
    down()
    for i in range(500):
        forward(i)
        forward(10)
        left(91)

def a(x):
    up()
    down()
    for i in range(1,300):
        forward((i*5))
        left(x)
        
def randomsetMaker():
    for i in range(1):
        x = random.random()
        y = random.random()
        xt = int(x*300) - 150
        yt = int(y*300) - 150
        up()
        shome(xt,yt)
        down()
        a89()
        up()
        shome(xt,yt)
        down()
        a90()
        up()
        shome(xt,yt)
        down()
        a91()
    up()
    shome(800,800)
        
def eternalFlower():
    a89()
    up()
    home()
    down()
    a90()
    up()
    home()
    down()
    a91()

a(90)
up()
home()
down()
a(120)
up()
home()
down()
a(60)

