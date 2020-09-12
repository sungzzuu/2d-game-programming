import turtle as t

scale = 100

def move_to(x, y):
	t.penup()
	t.goto(x, y)
	t.pendown()
	
def draw_nieun(xs = 1):
        x, y = t.pos()
        t.forward(scale*xs*0.5)
        t.left(90)
        t.forward(scale)
        move_to(x, y)
        
def draw_shiot(xs = 1):
        x, y = t.pos()
        move_to(x+ scale * 0.5, y)
        t.setheading(0)
        t.right(120)
        t.forward(scale)
        move_to(x+ scale * 0.5, y)
        t.setheading(0)
        t.right(60)
        t.forward(scale)
        move_to(x, y)

def draw_jieut(xs = 1):
        x, y = t.pos()
        t.forward(scale)
        move_to(x+ scale * 0.5, y)
        t.setheading(0)
        t.right(120)
        t.forward(scale)
        move_to(x+ scale * 0.5, y)
        t.setheading(0)
        t.right(60)
        t.forward(scale)
        move_to(x, y)

def draw_ieung(xs = 1):
	x, y = t.pos()
	move_to(x + scale * xs * 0.5, y - scale * 0.8)
	t.setheading(0)
	t.circle(scale * 0.4)
	move_to(x, y)

def draw_yu():
        x, y = t.pos()
        y2 = y - scale * 1.1
        move_to(x, y2)
        t.setheading(0)
        t.forward(scale)
        t.backward(scale * 0.6)
        t.right(90)
        t.forward(scale*0.2)
        move_to(x + scale * 0.6, y2)
        t.forward(scale * 0.2)
        move_to(x,y)
        
def draw_u():
        x, y = t.pos()
        t.setheading(0)
        t.forward(scale)
        move_to(x + scale *0.5, y)
        t.right(90)
        t.forward(scale)
        move_to(x,y)
        
def draw_eo():
        x,y = t.pos()
        x2 = x + scale * 1.2
        y2 = y - scale * 0.5
        move_to(x2, y2)
        t.goto(x2 + scale * 0.3, y2)
        move_to(x2 + scale * 0.3, y)
        t.goto(x2 + scale * 0.3, y - scale)
        move_to(x, y)
        
def draw_final(func = None):
	x, y = t.pos()
	if func != None:
		move_to(x, y - scale * 1.5)
		func()
	move_to(x + scale * 2, y)

def draw_final_right(func = None):
	x, y = t.pos()
	if func != None:
		move_to(x + scale *0.5, y - scale * 1.5)
		func()
	move_to(x + scale * 2, y)




move_to(-300, 200)

draw_ieung()
draw_yu()
draw_final(draw_nieun)

draw_shiot()
draw_eo()
draw_final_right(draw_ieung)

draw_jieut()
draw_final(draw_u)

t.exitonclick()
