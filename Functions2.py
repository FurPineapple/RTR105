Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> # Functions
>>> 
================== RESTART: /home/user/RTR105/Functions1.py ==================
Hello
Fun
Zip
Hello
Fun
>>> big=max("HELLO WORLD")
>>> print(big)
W
>>> tiny=min("hellow world")
>>> print(tiny)
 
>>> print(float(99)/100)
0.99
>>> i=42
>>> type(i)
<type 'int'>
>>> f=float(i)
>>> print(f\)
      
SyntaxError: unexpected character after line continuation character
>>> print(f)
42.0
>>> type(f\)
     
SyntaxError: unexpected character after line continuation character
>>> type(f)
<type 'float'>
>>> print(1+2*float(3)/4-5)
-2.5
>>> 
>>> sval=123
>>> type(sval)
<type 'int'>
>>> print(sval+1)
124
>>> sval='123'
>>> type(sval)
<type 'str'>
>>> print(sval+1)

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(sval+1)
TypeError: cannot concatenate 'str' and 'int' objects
>>> ival=int(sval)
>>> type(ival)
<type 'int'>
>>> print(ival+1)
124
>>> nsv='Hello Bob'
>>> niv=int(nsv)

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    niv=int(nsv)
ValueError: invalid literal for int() with base 10: 'Hello Bob'
>>> 
