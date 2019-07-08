import turtle, random
from turtle import *

turtle.speed(0)

j = 10;
while j <= 360:
  r = random.randint(1,360) 
  turtle.left(r)
  turtle.forward(j)
  turtle.backward(j)
  turtle.right(r)
  j+=1
