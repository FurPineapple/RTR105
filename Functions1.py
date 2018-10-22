# Functions
"""
def thing():
    print("Hello")
    print("Fun")
thing()
print("Zip")
thing()
"""
"""
x=5
print("Hello")

def print_lyrics():
    print("Hello, my lady.")
    print("Hello, my honey.")

print_lyrics()
print("My pleasure")
x=x+2
print(x)
"""
"""
def greet(lang):
    if lang=="es":
        print("Hola")
    elif lang=="fr":
        print("Bonjour")
    else:
        print("Hello")
greet("en")
greet("es")
greet("fr")
"""

"""
def greet():
    return "Hello"
#print(greet(),"Glenn") 3PYTHON
#print greet(),"Glenn"  2PYTHON

#print("%s %s"%(greet(),"Glenn")) STABILE VARIANT
print("%s %s"%(greet(),"Glenn"))
print("%s %s"%(greet(),"Sally"))
"""

""" 
def greet(lang):
    if lang== 'es':
        return'Hola'
    elif lang== 'fr':
        return 'Bonjour'
    else:
        return "Hello"
print("%s %s"%(greet('en'),"Glenn"))
print("%s %s"%(greet('es'),"Sally"))
print("%s %s"%(greet('fr'),"Michael"))
"""
"""
def addtwo(a,b):
    added=a+b
    return added
x=addtwo(3,5)
print(x)
"""

#Exercise
def computepay(hours,rate):
 if hours>40.0:
  p = rate * 40.0
  p = p+(1.5*rate*(hours-40))
 else:
  p = rate*hours
 return p
hours = float(raw_input("Enter worked hours: "))
rate = float(raw_input("Enter Pay rate per hour: "))
print (computepay(hours,rate))
