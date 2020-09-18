Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> pos[1]
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    pos[1]
NameError: name 'pos' is not defined
>>> import turtle
>>> pos = turtle.pos()
>>> pos[0]
0.0
>>> pos[1]
0.0
>>> x
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> x,y = pos
>>> x
0.0
>>> y
0.0
>>> pos = 123, 456
>>> pos[1]
456
>>> turtle.goto(*pos)
>>> x
0.0
>>> y
0.0
>>> t = x
>>> turtle.setheading(90)
>>> for i in range(1, 10+1)
SyntaxError: invalid syntax
>>> for i in range(1, 10+1):
	print(i)

	
1
2
3
4
5
6
7
8
9
10
>>> for i in range(1, 10):
	print(i)

	
1
2
3
4
5
6
7
8
9
>>> 