import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import arcsinh, linspace
def f(x):
    return arcsinh(x)
x=linspace(0,4,11)
print(x)
y=f(x)
print(y)

deltax=x[1]-x[0]
N=len(x)
atvasinajums=[]

for i in range(N):
    #diferencešanas formula
    temp=(f(x[i]+deltax)-f(x[i]))/deltax
    atvasinajums.append(temp)
    print(atvasinajums)

atvasinajums_caur_massivu=[]
for i in range(N-1):
    temp=(y[i+1]-y[i])/(x[i+1]-x[i])
    atvasinajums_caur_massivu.append(temp)
