import turtle
turtle.title("I LUV U By Turtle")
t = turtle.Turtle()
t.shape('turtle')

def Rectangle():
    t.pencolor('red')
    t.fillcolor('red')
    t.begin_fill()
    for i in range(4):
        t.fd(50)
        t.rt(90)
    t.end_fill()

def Go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def Line():
    t.pensize(5)
    t.pencolor('red')
    t.fillcolor('red')
    t.fd(850)
    
# I
Go(-400,0)
Rectangle()
Go(-400,-50)
Rectangle()
Go(-400,-100)
Rectangle()
# LUV
Go(-250,0) #L
Rectangle()
Go(-250,-50)
Rectangle()
Go(-250,-100)
Rectangle()
Go(-200,-100)
Rectangle()
Go(-125,0) #U
Rectangle()
Go(-125,-50)
Rectangle()
Go(-125,-100)
Rectangle()
Go(-75,-100)
Rectangle()
Go(-25,-100)
Rectangle()
Go(-25,-50)
Rectangle()
Go(-25,0)
Rectangle()
Go(50,0) #V
Rectangle()
Go(50,-50)
Rectangle()
Go(100,-100)
Rectangle()
Go(150,-50)
Rectangle()
Go(150,0)
Rectangle()
#U
Go(300,0)
Rectangle()
Go(300,-50)
Rectangle()
Go(300,-100)
Rectangle()
Go(350,-100)
Rectangle()
Go(400,-100)
Rectangle()
Go(400,-50)
Rectangle()
Go(400,0)
Rectangle()

turtle.bgcolor("pink")

Go(-400,50)
Line()
Go(-400,-200)
Line()
