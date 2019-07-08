import turtle, random
from turtle import *

turtle.speed(0)
#turtle.bgcolor('blue')

turtle.pencolor("red")
k = 90;
while k <= 180:
  for r1 in range(0,360):
    turtle.left(r1)
    turtle.forward(k)
    turtle.backward(k)
    turtle.right(r1)
    k+=1
'''
j = 10;
while j <= 360:
  turtle.pencolor("green")
  r = random.randint(1,360) 
  turtle.left(r)
  turtle.forward(j)
  turtle.backward(j)
  turtle.right(r)
  j+=1

'''
l = 1
turtle.pencolor("green")
while l <= 90:
  for r2 in range(0,360):
    turtle.left(r2)
    turtle.forward(l)
    turtle.backward(l)
    turtle.right(r2)
    l+=1
