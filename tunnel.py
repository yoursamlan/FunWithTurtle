import turtle, random
from turtle import *

turtle.speed(0)
'''
j = 100;
while j <= 360:
  r = random.randint(1,300)
  turtle.forward(j)
  turtle.left(r)
  turtle.backward(j)
  j+=10
'''
j = 10;
while j <= 360:
  for r in range(0,360):
    turtle.forward(j)
    turtle.left(r)
    turtle.backward(j)
    j+=1
