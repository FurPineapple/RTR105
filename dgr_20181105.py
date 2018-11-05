Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> str1="Hello"
>>> str2="there"
>>> bob= str1+str2
>>> print(bob)
Hellothere
>>> str3="123"
>>> str3=str3+1
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    str3=str3+1
TypeError: must be str, not int
>>> x=int(str3)+1
>>> print(x)
124
>>> 
>>> 
>>> name=input("Enter")
EnterChuck
>>> print(name)
Chuck
>>> apple=input("Enter")
Enter100
>>> x=apple-10
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    x=apple-10
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> x=int(apple)-10
>>> print(x)
90
>>> 
>>> 
>>> fruit="banana"
>>> letter=fruit[1]
>>> print(letter)
a
>>> letter=fruit[0]
>>> print(letter)
b
>>> letter=fruit[1]
>>> x=3
>>> w=fruit[x-1]
>>> print(w)
n
>>> 
>>> 
>>> zot="abc"
>>> print(zot[5])
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print(zot[5])
IndexError: string index out of range
>>> print(zot[2])
c
>>> 
>>> 
>>> fruit="banana"
>>> print(len(fruit))
6
>>> 
>>> 
>>> fruit="banana"
>>> x=len(fruit)
>>> print(x)
6
>>> 
>>> 
>>> 
=================== RESTART: /home/user/RTR105/strings1.py ===================
0 b
1 a
2 n
3 a
4 n
5 a
>>> 
=================== RESTART: /home/user/RTR105/strings1.py ===================
b
a
n
a
n
a
>>> 
=================== RESTART: /home/user/RTR105/strings1.py ===================
b
a
n
a
n
a
b
a
n
a
n
a
>>> 
=================== RESTART: /home/user/RTR105/strings1.py ===================
3
>>> 
>>> 
>>> s="Monty Python"
>>> print(s[0:4])
Mont
>>> print(s[6:7])
P
>>> print(s[4:9])
y Pyt
>>> 
>>> 
>>> s="Monty Python"
>>> print(s[:])
Monty Python
>>> 
>>> 
>>> a="Hello"
>>> b=a+"There"
>>> print(b\)
	  
SyntaxError: unexpected character after line continuation character
>>> print(b)
	  
HelloThere
>>> c=a+" "+"There"
	  
>>> print(c)
	  
Hello There
>>> 
	  
>>> 
	  
>>> fruit="banana"
	  
>>> "n" in fruit
	  
True
>>> "m" in frit
	  
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    "m" in frit
NameError: name 'frit' is not defined
>>> "m" in fruit
	  
False
>>> if "a" in fruit:
	  print("Fount it")

	  
Fount it
>>> 
	  
>>> 
	  
>>> 
=================== RESTART: /home/user/RTR105/strings1.py ===================
Traceback (most recent call last):
  File "/home/user/RTR105/strings1.py", line 37, in <module>
    if word=="banana":
NameError: name 'word' is not defined
>>> 
=================== RESTART: /home/user/RTR105/strings1.py ===================
3
all right, bananas
All right, bananas.
>>> 
=================== RESTART: /home/user/RTR105/strings1.py ===================
Enter word:bananaaas
5
Your word,bananaaas,comes after banana.
>>> 
	  
>>> 
	  
>>> greet="Hello Bob"
	  
>>> zap=greet.lower()
	  
>>> print(zap)
	  
hello bob
>>> print(greet)
	  
Hello Bob
>>> print("Hi There,".lower())
	  
hi there,
>>> print("Hi There,".lower()greet)
	  
SyntaxError: invalid syntax
>>> print("Hi There,".lower(),greet)
	  
hi there, Hello Bob
>>> 
	  
>>> 
	  
>>> stuff="Hello world"
	  
>>> type(stuff)
	  
<class 'str'>
>>> dir(stuff)
	  
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
	  
>>> 
	  
>>> fruit="banana"
	  
>>> pos=fruit.find("na")
	  
>>> print(pos)
	  
2
>>> aa=fruit.find("z")
	  
>>> print(aa)
	  
-1
>>> 
	  
>>> 
	  
>>> greet="Hello Bob"
	  
>>> nnn=greet.upper()
	  
>>> print(nnn)
	  
HELLO BOB
>>> www=greet.lower()
	  
>>> print(www)
	  
hello bob
>>> 
	  
>>> 
	  
>>> greet="Hello Bob"
	  
>>> nstr=greet.replace("Bob","Jane")
	  
>>> print(nstr)
	  
Hello Jane
>>> nstr=greet.replace("o","X")
	  
>>> print(nstr)
	  
HellX BXb
>>> 
	  
>>> 
	  
>>> greet="Hello Bob"
	  
>>> greet.lstrip()
	  
'Hello Bob'
>>> greet.rstrip()
	  
'Hello Bob'
>>> greet.strip()
	  
'Hello Bob'
>>> 
	  
>>> 
	  
>>> line="Please have a nice day"
	  
>>> line.startswith("Please")
	  
True
>>> line.startswith("p")
	  
False
>>> 
	  
>>> 
	  
>>> 
KeyboardInterrupt
data
= 
'From 
stephen.marquard@uct.ac.za
Sat Jan  5 09:14:16 2008'
>>> data='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
	  
>>> atpos=data.find("@")
	  
>>> print(atpos)
	  
21
>>> sppos=data.find(" ",atpos)
	  
>>> print(sppos)
	  
31
>>> host=data[atpos+1:sppos]
	  
>>> print(host)
	  
uct.ac.za
>>> 
	  
>>> 
	  
>>> x="21fvuy"
	  
>>> type(x)
	  
<class 'str'>
>>> x=u"21fvuy"
	  
>>> type(x)
	  
<class 'str'>
>>> 
	  
>>> 
	  
>>> 
