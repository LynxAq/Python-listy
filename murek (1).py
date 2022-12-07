import turtle
from turtle import *
import numpy as np


def kwadrat(bok):
    colour = np.random.rand(1, 3)
    color(colour)
    begin_fill()
    for i in range(4):
      fd(bok)
      rt(90)
    end_fill()
    
def murek(s,bok):
  for a in s:
     if a == 'f':
         kwadrat(bok)
         fd(bok)
     elif a == 'b':
         kwadrat(bok)
         fd(bok)         
     elif a == 'l':
         bk(bok)
         lt(90)
     elif a == 'r':
        rt(90)
        fd(bok)
string1 = ''
for i in range(0,17):
    string1 = string1 + (i+1) * 'f' + 'r'


ht()

tracer(0,0) # szybkie rysowanie     
#murek('fffffffffrfffffffffflfffffffffrfffffl',10)
turtle.penup()
turtle.setposition(200,120)
turtle.pendown()
murek(4* 'ffffr', 14)
turtle.penup()
setposition(0,0)
turtle.pendown()
murek(string1,14)
update() # uaktualnienie rysunku

turtle.exitonclick()
