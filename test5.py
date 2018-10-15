#rawstr=input("Enter a number:")

ival = 1
try:
    rawstr=input("Enter a number:")
    #ival=int(rawstr)
except:
    ival=-1

if ival>0:
    print("Nice work")
else:
    print("Not a number")

#if ival == str:
#    print("Not a number")
