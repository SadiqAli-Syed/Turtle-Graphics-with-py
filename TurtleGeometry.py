from turtle import Turtle,Screen
from random import choice
t=Turtle()
t.pensize(2)
t.penup()
t.setpos(x=0, y=170)
t.pendown()
t.shape("turtle")
l=[1,2,3,4,5,6,7,8,9,0,"a","b","c","d","e","f"]
c=""
def col(c):
    c=c+str(choice(l))
    if len(c)<6:
        return col(c)
    else:
        return c
c=col(c)
for i in range(3,11):
    a=360/i
    t.backward(5)
    c=""
    c=col(c)
    c="#"+c
    t.color(c)
    for j in range(i):
        t.forward(10*i)
        t.right(a)

t.forward(50)
s=Screen()
s.exitonclick()