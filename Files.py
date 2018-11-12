"""
xfile=open("wtcher.txt")
for visual in xfile:
    print(visual)
"""
"""
fhand=open("wtcher.txt")
count=0
for line in fhand:
    count=count+1
print("Line count: ", count)
"""

"""
fhand=open("wtcher.txt")
count=0
for visual in fhand:
    print(visual)
    count=count+1
print("Line count: ", count)
"""

"""
fhand=open("wtcher.txt")
for line in fhand:
    if line.startswith("#"):
        print(line)
"""

"""
fhand=open("wtcher.txt")
for line in fhand:
    line=line.rstrip()
    if line.startswith("#"):
        print(line)
"""

"""
fhand=open("wtcher.txt")
for line in fhand:
    line = line.rstrip()
    if not line.startswith("$"):
        continue
    print(line)
"""

"""
fname=input("Enter the file name: ")
try:
    fhand=open(fname)
except:
    print("File cannot be opened", fname)
    quit()

count=0
for line in fhand:
    if line.startswith("#"):
        count=count+1
print("There were",count,"subject line in",fname)
"""
