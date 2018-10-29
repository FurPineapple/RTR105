"""
while True:
    line=input(">")
    if line == "done":
        break
    print(line)
print("done")
"""

"""
while True:
    line=input(">")
    if line[0]=="$":
        continue
    if line=="done":
        break
    print(line)
print("done")
"""

"""
for i in ["curl","wavy","black"]:
    print(i)
print("PARTY")
"""

"""
friends=["Joseph","Glenn","Sally"]
for friend in friends:
    print("Happy New Year:",friend)
print("Done")
"""

"""
largest_so_far=-1
print("Before:",largest_so_far)
for num in [9,12,54,15,103,98,104,-125]:
    if num>largest_so_far:
        largest_so_far=num
    print(largest_so_far,num)
print("After",largest_so_far)
"""

"""
zork=0
print("Before",zork)
for num in [9,1,83,-2,66,15]:
    zork=zork+num
    print(zork,num)
print("After",zork)
"""

"""
count=0
sum=0
print("Before",count,sum)
for value in [9,12,-20,54,46,0.5]:
    count=count+1
    sum=sum+value
    print(count,sum,value)
print("After",count,sum,sum/count)
"""

"""
print("Before")
for value in [9,-2,41,73.5,867.003,15/0.0015]:
    if value>20:
        print("Large number",value)
print("After")
"""

"""
found=False
print("Before",found)
for value in [-12,0.783,16,25,15,9,4,74]:
    if value==25:
        found=True
    print(found,value)
print("After",found)
"""

"""
small=None
print("Before")
for num in [9,-1.119,15,18]:
    if small is None:
        small=num
    elif num<small:
        small=num
    print(small,num)
print("After",small)
"""
