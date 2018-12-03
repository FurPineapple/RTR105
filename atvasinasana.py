import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import sin, linspace
def f(x):
    return sin(x)

x=linspace(0,4,11)
print(x)
y=f(x)
#y=sin(x)
print(y)
legend=[]

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("$sin(x)$ funkcija un tās atvasinajumi")
plt.plot(x,y,"k")

legend.append("$sin(x)$ funkcijas")
plt.plot(x,y,"go")

legend.append("$sin(x)$ funkcija(daži punkti)")
plt.plot(x,y,"go")

deltax=x[1]-x[0]
N=len(x)
atvasinajums=[]

for i in range(N):
    #diferencešanas formula
    temp=(f(x[i]+deltax)-f(x[i]))/deltax
    atvasinajums.append(temp)
    print(atvasinajums)

plt.plot(x,atvasinajums,"y")
legend.append("atvasinājums")

plt.plot(x,atvasinajums,"ro")
legend.append("atvasinājums(daži punkti)")

atvasinajums_caur_massivu=[]
for i in range(N-1):
    temp=(y[i+1]-y[i])/(x[i+1]-x[i])
    atvasinajums_caur_massivu.append(temp)

plt.plot(x[0:N-1],atvasinajums_caur_massivu,"m")
legend.append("atvasinājums(izmantojot vertibas no masiva)")

plt.plot(x[0:N-1],atvasinajums_caur_massivu,"bo")
legend.append("atvasinājums(izmantojot vertibas no massiva; daži punkti)")
#print(plt.legend.__doc__)

plt.legend(legend,loc=3)#attēlot grafiku
plt.show()
