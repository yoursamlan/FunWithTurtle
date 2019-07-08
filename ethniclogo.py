import turtle, random
from turtle import *

turtle.speed(0)
#turtle.bgcolor('blue')
turtle.left(90)
turtle.pencolor("red")
k = 0;
while k <= 180:
  for r1 in range(0,180):
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
turtle.pencolor("blue")
while l <= 90:
  for r2 in range(180,360):
    turtle.left(r2)
    turtle.forward(l)
    turtle.backward(l)
    turtle.right(r2)
    l+=1
l1 = 1
turtle.pencolor("green")
while l1 <= 90:
  for r3 in range(270,540):
    turtle.left(r3)
    turtle.forward(l1)
    turtle.backward(l1)
    turtle.right(r3)
    l1+=1
l2 = 1
turtle.pencolor("yellow")
while l2 <= 90:
  for r4 in range(720,900):
    turtle.left(r4)
    turtle.forward(l2)
    turtle.backward(l2)
    turtle.right(r4)
    l2+=1
