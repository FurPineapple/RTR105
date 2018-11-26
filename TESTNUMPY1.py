import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

#print(vars())

from numpy import cos, sin, linspace

#x = linspace(0, 7, 70) #solis = (7-0)/(70-1)
x = linspace(0, 4, 11) #solis = (4-0)(11-1)
y = cos(x)
y1 = sin(x)
#print(vars())

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $cos(x)$ un $sin(x)@')
plt.plot(x, y, color = "#FF1588")
plt.plot(x, y1, color = "#00BB66")
plt.plot(x, y1, "bo")
plt.plot(x, y, "ko")
plt.legend(["$cos(x)$", "$cos(x)$", "$sin(x)$", "$sin(x)$"])
plt.show()
