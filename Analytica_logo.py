#Analytica LOGO
import turtle 

colors = ['purple', 'blue', 'green', 'orange', 'yellow','red'] 
t = turtle.Pen() 
turtle.bgcolor('black')
t.speed(0)
while True:
    for x in range(120): 
        t.pencolor(colors[x%6]) 
        t.width(x/100 + 1) 
        t.forward(x) 
        t.left(58)
        
