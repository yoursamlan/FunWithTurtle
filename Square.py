import turtle
from turtle import *

print ('Enter the side length of Square: ')
val = input()
for i in range (4):
    turtle.forward(int(val))
    turtle.right(90)
