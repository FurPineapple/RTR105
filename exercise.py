'''
hrs=input("Enter your hours: ")
h=float(hrs)
rate=input("Enter your rate: ")
r=float(rate)
if h>40:
    pay=40*r+(h-40)*15
else:
    pay=r*h
print(pay)
'''

try:
    hrs=input("Enter Hours: ")
    hr=float(hrs)
except:
    hr="Error, please enter numeric input"
    print(hr)
try:
    rate=input("Enter Rate per hour: ")
    rt=float(rate)
except:
    rt="Error, please enter numeric input"
    print(rt)
if hr>40:
    pay=40*rt+(hr-40)*rt*1.5
else:
    pay=hr*rt
print(pay)
