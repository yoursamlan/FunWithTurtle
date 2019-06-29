#It's the funniest way to draw X on a graph paper
import turtle
from turtle import *

for i in range (20,500,10):
    turtle.forward(int(i))
    turtle.right(90)
    for j in range (20,100,10):
        turtle.forward(int(i-j))
        turtle.right(90)
        for k in range (20,50,50):
            turtle.forward(int(i+k))
            turtle.right(90)
