Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> print(123)
123
>>> print(98.2)
98.2
>>> print("Hello Wolrld!")
Hello Wolrld!
>>> x=12.2
>>> y=14
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 12.2, 'y': 14, '__name__': '__main__', '__doc__': None}
>>> x=100
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 100, 'y': 14, '__name__': '__main__', '__doc__': None}
>>> spam23=x
>>> _speed=y
>>> vars()
{'spam23': 100, '__builtins__': <module '__builtin__' (built-in)>, '_speed': 14, '__package__': None, 'x': 100, 'y': 14, '__name__': '__main__', '__doc__': None}
>>> spam23
100
>>> _speed
14
>>> Spam23=25
>>> vars()
{'spam23': 100, 'Spam23': 25, '__builtins__': <module '__builtin__' (built-in)>, '_speed': 14, '__package__': None, 'x': 100, 'y': 14, '__name__': '__main__', '__doc__': None}
>>> "mnemotic"="memory aid"
SyntaxError: can't assign to literal
>>> mnemotic="memory aid"
>>> x1q3z9ocd=35.0
>>> x1q3z9afd=12.50
>>> x1q3p9afd=x1q3z9ocd*x1q3z9ad

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    x1q3p9afd=x1q3z9ocd*x1q3z9ad
NameError: name 'x1q3z9ad' is not defined
>>> x1q3p9afd=x1q3z9ocd*x1q3z9afd
>>> print(x1q3p9afd)
437.5
>>> hours=35.0
>>> rate=12.50
>>> pay=hours*rate
>>> print(pay)
437.5
>>> x=2
>>> x=x+2
>>> print(x)
4
>>> x=3.9*x*(1-x)
>>> print(x)
-46.8
>>> x=0.6
>>> x=3.9*x*(1-x)
>>> print(x)
0.936
>>> x=3.9*x*(1-x)
>>> print(x)
0.2336256
>>> xx=2
>>> xx=xx+2
>>> print(xx)
4
>>> yy=440*12
>>> print(yy)
5280
>>> zz=yy/1000
>>> print(zz)
5
>>> 5/2
2
>>> 5.00/2.00
2.5
>>> zz=yy.00/1000
SyntaxError: invalid syntax
>>> yy=440.00*12.00
>>> print(yy)
5280.0
>>> zz=yy/1000
>>> print(zz)
5.28
>>> jj=23
>>> kk=jj%5.00
>>> print(kk)
3.0
>>> print(4**3)
64
>>> x=1+2*3-4/5**6
>>> print(x)
7
>>> ddd=1+4
>>> print(ddd)
5
>>> eee="hello"+"there"
>>> print(eee)
hellothere
>>> eee="hello" + "there"
>>> print(eee)
hellothere
>>> eee="hello " + "there"
>>> print(eee)
hello there
>>> eee=eee+1

Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    eee=eee+1
TypeError: cannot concatenate 'str' and 'int' objects
>>> type(eee)
<type 'str'>
>>> type("hello")
<type 'str'>
>>> type(1)
<type 'int'>
>>> 2.5*2
5.0
>>> xx=1
>>> type(xx)
<type 'int'>
>>> temp=98.6
>>> type(temp)
<type 'float'>
>>> type(1)
<type 'int'>
>>> type(1.0)
<type 'float'>
>>> print(float(99)+100)
199.0
>>> i=42
>>> type(i)
<type 'int'>
>>> f=float(i)
>>> print(d)

Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    print(d)
NameError: name 'd' is not defined
>>> print(f)
42.0
>>> type(f)
<type 'float'>
>>> print(10/2)
5
>>> print(9./2)
4.5
>>> print(99./100)
0.99
>>> print(10.0/2.0)
5.0
>>> print(99./100.)
0.99
>>> sval=(123)
>>> tupe(sval)

Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    tupe(sval)
NameError: name 'tupe' is not defined
>>> type(sval)
<type 'int'>
>>> print(sval+1)
124
>>> ival=int()
>>> ival=int(sval)
>>> type(sval)
<type 'int'>
>>> print(ival+1)
124
>>> ival
123
>>> nsv="hello bob"
>>> niv=int(nsv)

Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    niv=int(nsv)
ValueError: invalid literal for int() with base 10: 'hello bob'
>>> nam=input("who are you?")
who are you?Bob

Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    nam=input("who are you?")
  File "<string>", line 1, in <module>
NameError: name 'Bob' is not defined
>>> nam=input("who are you?")
who are you? bob

Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    nam=input("who are you?")
  File "<string>", line 1, in <module>
NameError: name 'bob' is not defined
>>> print("welcome," nam)
SyntaxError: invalid syntax
>>> nam=input("who are you? ")
who are you? Bob\

Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    nam=input("who are you? ")
  File "<string>", line 1
    Bob\
       ^
SyntaxError: unexpected character after line continuation character
>>> nam=input("who are you? ")
who are you? Bob

Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    nam=input("who are you? ")
  File "<string>", line 1, in <module>
NameError: name 'Bob' is not defined
>>> nam=input("who are you? ")
who are you? Bob

Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    nam=input("who are you? ")
  File "<string>", line 1, in <module>
NameError: name 'Bob' is not defined
>>> nam=raw_input("who are you? ")
who are you? Bob
>>> nam
'Bob'
>>> inp=input("Europe floor? ")
Europe floor? 0
>>> usf=int(inp)+1
>>> print("US floor", usf)
('US floor', 1)
>>> # Get the name of the file and open it
>>> # Get the name of the file and open it
>>> name=raw_input("Enter file name: ")
Enter file name: text.txt
>>> name
'text.txt'
>>> hanlde=open(name, "r")
>>> nandle

Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    nandle
NameError: name 'nandle' is not defined
>>> hanlde
<open file 'text.txt', mode 'r' at 0x7f6b5dd808a0>
>>> hanlde=open("text.txt","r")
>>> hanlde
<open file 'text.txt', mode 'r' at 0x7f6b5dc10e40>
>>> # Coount world frequency
>>> counts=dict()
>>> for line in hanlde:
	words=line.split()
	for word in words:
		counts[word]=counts.get(word,0)+1

		
>>> # Find the most common word
>>> bigcount=None
>>> bigword=None
>>> for word,count in counts.items():
	if bigcount is None or count>bigcount:
		bigword=word
		bigcount=count

		
>>> #all done
>>> print(bigword, bigcount)
('iehfw', 1)
>>> hr=input("Enter Hours")
Enter Hours35
>>> rt=input("Enter Rate")
Enter Rate2.75
>>> pay=rt
>>> pay=rt*hr
>>> print(pay)
96.25
>>> 
