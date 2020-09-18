import turtle

turtle.goto(0,0)
for i in range(0,6):
    turtle.goto(0, i*100)
    turtle.pendown()
    turtle.goto(500, i*100)
    turtle.penup()
    
turtle.goto(0,0)
for i in range(0,6):
    turtle.goto(i*100, 0)
    turtle.pendown()
    turtle.goto(i*100, 500)
    turtle.penup()
