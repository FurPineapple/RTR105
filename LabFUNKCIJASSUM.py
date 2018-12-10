from math import asinh
import math

def fasinh(x):
    k=0
    a=0
    S=a
    print("Izdruka no liet.f. a0=%6.2f S0=%6.2f"%(a,S))

    while k<500:
        k=k+1
        R=()
    a=0
    S=S+a
    if k==499:
        print("Izdruka no liet.f.a%d=%6.2fS%d=%6.2f"%(k,a,k,S))
    print("Izdruka no liet.f. a500=%6.2f S500=%6.2f"%(a,S))
    return S
x=float(input("Lietotajs, ludzu, ievadi argmumentu(x):"))
y=asinh(x)
print("asinh(%.2f)=%6.2f"%(x,y))

yy=fasinh(x)
print("fasinh(%.2f)=%6.2f"%(x,yy))

print("                500                              ")
print("             ____________                        ")
print("             \            k                2k+1  ")
print("              \       (-1)! * (2*k)!  * (x)      ")
print("ahinh()%.2f)=  \  ____________________________   "%(x))
print("               /    k      2                     ")
print("              /    4  * (k!) * (2*k+1)            ")
print("             /___________                        ")
print("                  k = 0                          ")
