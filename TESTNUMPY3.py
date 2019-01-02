#f(x)=arcsinh(x) Attēlotā funkcijā krustojuma punkts ir noverots,
#f(x)=0, kad x=3,14159+pi*n, kur n=Z.

from math import asinh,fabs
from time import sleep

def f(x):
    return asinh(x)
k=0
# Definejam argumenta x robežas:
a=-1
b=2
# Apreķinam funkcijas vērtības dotajos punktos:
funa=f(a)
funb=f(b)
# Pārbaudam, vai dotajā intervālā ir saknes:
if(funa*funb>0.0):
    print("Dotajā intervālā[%s,%s] sakņu nav"%(a,b))
    sleep(1);exit()     #Ziņo uz ekrāna, gaida 1 sec. un darbu pabeidz
else:
    print("Dotajā intervālā sakne(s) ir!")
# Definējam precizitāti, ar kādu meklēsim sakni:
deltax=0.000000000000001
# Sašaurinam saknes meklēšanas robežas:
while(fabs(b-a)>deltax):
    x=(a+b)/2;funx=f(x)
    if (funa*funx<0.):
        b=x
        k=k+1
    else:
        a=x
print("Sakne ir: ",x)
print("f(x)=", asinh(x))
print("k=", k)
