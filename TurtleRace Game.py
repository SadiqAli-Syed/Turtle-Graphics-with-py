from turtle import Turtle, Screen, textinput
from random import randint
c = textinput("Color", "Please Enter the Color You want to bet on: ")
bx=-370
by=250
y=Turtle()
y.pensize(5)
y.color("red")
y.penup()
y.setpos(x=352.5, y=-300)
y.left(90)
y.pendown()
y.forward(700)
def trtl(color):
    global bx, by
    a=Turtle()
    a.penup()
    a.setpos(x=bx,y=by)
    a.pendown()
    by-=100
    a.shape("turtle")
    a.color(color)
    a.penup()
    a.speed("fastest")
    return a
r=trtl("red")
g=trtl("green")
b=trtl("blue")
y=trtl("yellow")
lb=trtl("light blue")

t=[r, g, b, y, lb]
flag=True
def frwd():
    global flag
    while flag:
        for i in t:
            i.forward(randint(1,3))
            if i.xcor()>=335:
                flag=False
                if i.color()[0]==c:
                    print(f"Your Bet was Correct!,The {i.color()[0]} Coloured Turtle Wins,So do YOU!")
                else:
                    print(f"You Lost your Bet, '{i.color()[0]}' Won Instead of '{c}'")
                break
  

s=Screen()
s.onkey(frwd, "Right")
s.listen()
s.exitonclick()