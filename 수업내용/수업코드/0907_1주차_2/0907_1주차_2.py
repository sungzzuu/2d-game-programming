Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> pi = 32322
>>> pi
32322
>>> a = p = pi
>>> a
32322
>>> s = "'Hello"
>>> s
"'Hello"
>>> s = Hello
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    s = Hello
NameError: name 'Hello' is not defined
>>> s = "Hello"
>>> s
'Hello'
>>> type(s)
<class 'str'>
>>> 'hello' * 5
'hellohellohellohellohello'
>>> 'hello ' * 5
'hello hello hello hello hello '
>>> [10,20)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> 