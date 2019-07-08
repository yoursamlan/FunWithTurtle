import turtle, random
from turtle import *

turtle.speed(0)
#turtle.bgcolor('blue')

turtle.pencolor("red")
k = 1;
while k <= 360:
  for r1 in range(0,720):
    turtle.left(r1)
    turtle.forward(k)
    turtle.backward(k)
    turtle.right(r1)
    k+=1
j = 10;
while j <= 360:
  turtle.pencolor("green")
  r = random.randint(1,360) 
  turtle.left(r)
  turtle.forward(j)
  turtle.backward(j)
  turtle.right(r)
  j+=1

