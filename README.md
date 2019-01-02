## RTR105
Dattormācības kursa elektroniskā klade

# Darbs LINUX
## Tab
- ātra izsaukšana
## Ctrl+Alt+T
- ieslēgt Terminālu:
> Open terminal  
## Ctrl+Shift+T
- vairākie logi:
> New log  
## Ctrl+Alt+F1...F7
- mainīt konsoli:
> another console  
## U+Tab+Tab
- iespējas:
> Display all possibilities  
### . / ..
- tekošas māpes vieta / māpe limenī augstāk:
> current location / higher level dirrectory 
# Papildus komandas
## command > * .txt  
- ispildīt comandu .txt failā:
> execute command in .txt file
### > file. *   
- uztaisīt failu:
> make a new file
### command > folder/ file. * 
- uztaisīt jaunu failu folder/ direktorijā
> make a new file in folder/
### echo +"text" > * .txt
- uzrakstīt tekstu:
> write a text  
### echo + "text" >> * .txt
- papildināt teksta failu:
> fill in some text  
## command+&
- turpināt darbību:
> continue  
## LS+ -a
- apraksts:
> Info  
## LS+ -l
- māpes apraksts:
> Dirrectory Info  
## LS+ -al
- detalizēta informācija:
> Accurate Info  
## LS+ -R
> Shows files/dirs and it's levels
## MAN+command
- vairāk informācijas par komandu:
> More Info  
## (zvaigzne * )
- lai izvēleties kādu objekta kopu:  
> rm bin/(zvaigzne * ).txt - remove all .txt objects; bin/ dirrectory
## -Y
- jā:
> Yes  
## -N
- nē:
> No  
# Language
## UNAME
- sistēmas nosaukums:
> System information  
## echo $0
- valodas informācija:
> Language Info  
## sh
- ieēt valodā sh:
> Enter Language sh  
## bash
- ieēt valodā bash:
> Enter Language bash  
## Python
- ieēt prog. valodā PYTHON:
> Enter Language PYTHON  
## Ipython
- ieēt prog. valodā IPYTHON:
> Enter Language IPYTHON  
## Idle
- ieēt prog. valodā IDLE:
> Enter Language IDLE  
## exit
- iziet:
> Exit  
# Starter Commands
## Who  
- kas pielagojies:  
> Show who is logged in    
## WhoAmI  
- lietotajvards  
> USERNAME  
## WhereIs  
- atrast vienkāršu failu:  
> locate a file  
## find  
- atrast failu direktorijā  
> search for file in dirrectory  
## sort  
- šķirot failus  
> sort files  
## clear  
- notīrīt terminālu  
> clear terminal  
## History  
- vēsture:  
> history  
## RM
- nodzēst failu/māpi:
> remove an object (-r) - to remove ignoring troubles (--forse)  
## LS
- attēlo māpes:
> Show Enabled Dirrectory
## CD
- kustīties caur direktorijām:
> move through dirrectories
## CD+ ~/
- mājas:
> home  
## CD + /home/user/
- mājās:
> home
## CP +object +"object name"
- kopēt:
> copy  
## MV + object1 + object2 = object2
- parsaukšana
> rename
## nano + object
- atvert redaktoru nano
> open nano editor
# Dirrectory moves
## MKDIR
- uztaisīt māpe:
> make dirrectory  
## RMDIR
- nodzēst māpe:
> remove dirrectory (-ignore-fail-or-non-emtpy)- to remove ignoring troubles 
## MV +Object +Dirrectory
- pārcelt objektu:
> move object  
> **MV +(Object * ) + Dirrectory**
- parvietot visus (Object) failus
> **MV +(Dirrectory1 ( * .txt)) +Dirrectory2**
- parcelt visus .txt objektus no (Dirrectory1) uz Dirrectory2
## chmod
> rwx rwx rwx (111 110 000)
> permission to the content

# File reading
## head(from the top)/tail(from the bottom)
> displays a text
> -n lines number
## CAT
- Objektu lasīšana:
> Shows text
## grep
> provides search in the text document
## cut
> is a command line utility for cutting sections from each line of 
> files and writing the result to standard output
>
> *FILE _ NAMES.CSW*
> John,Smith,34,London
> Arthur,Evans,21,Newport
> George,Jones,32,Truro
>
> cut -d ',' -f 1,4 names.csv
> John,London
> Arthur,Newport
> George,Truro
>
  

# PYTHON/IDLE

## Modules
> *#Import built-in module math*
> import math
> content = dir(math)
> print content
> *['__doc__', '__file__', '__name__', 'acos', 'asin', 'atan',   
> 'atan2', 'ceil', 'cos', 'cosh', 'degrees', 'e', 'exp',         
> 'fabs', 'floor', 'fmod', 'frexp', 'hypot', 'ldexp', 'log',     
> 'log10', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh',        
> 'sqrt', 'tan', 'tanh']*  
## print()
> describes an object
> type()
> * INTEGERS (int(a) )
> * FLOATING (float(a.) )
> * STRING (str("a") )
# BASIC MATHS 1
>  * (+) ADDITION
>  * (-) SUBTRACTION
>  * (*) MULTIPLICATION
>  * (/) DIVISION
>  * (**) POWER
>  * (%) REMAINDER
# BASIC MATHS 2
> (<) Less than

> (<=)  Less than or Equal to

> (==)  Equal to

> (>=)  Greater than or Equal to

> (>) Greater than

> (!=)  Not Equal
# BASIC MATHS 3
> len((1, 2, 3)) = 3  
> (1, 2, 3) + (4, 5, 6) = (1, 2, 3, 4, 5, 6)  
> ('Hi!',) * 4 = ('Hi!', 'Hi!', 'Hi!', 'Hi!')  
> 3 in (1, 2, 3) = true  
> for x in (1, 2, 3): print x, = true  
> 
## Strings
- To access substrings, use the square brackets   
- for slicing along with the index or indices to obtain your substring.  
> var1 = 'Hello World!'  
> var2 = "Python Programming"    

> print "var1[0]: ", var1[0]  
> print "var2[1:5]: ", var2[1:5]    
## Functions
# def
> # Function definition is here  
> def printme( str ):  
>    "This prints a passed string into this function"  
>    print str  
>    return;  

>  *Now you can call printme function*  
> printme("I'm first call to user defined function!")  
> printme("Again second call to the same function")  

## Lists
> list1 = ['physics', 'chemistry', 1997, 2000];  
> list2 = [1, 2, 3, 4, 5, 6, 7 ];  
> print "list1[0]: ", list1[0]  
> print "list2[1:5]: ", list2[1:5]  

## Operators

# if
> *if number in (range:[1,2,3...])*
# for
> *rangelist=range(10)*  

> *print(rangelist)*  

> *[0,1,2,3,4,5,6,7,8,9]*  

> *for number in (rangelist)*  
# while
> *while rangelist[1]==1:*

> *pass*(DOING NOTHING)
# else
> *else:*

> *continue*(DOING THE SAME, AGAIN)
# elif  
 var = 100  
 *if var == 200:*  
    print "1 - Got a true expression value"  
    print var  
 elif var == 150:  
    print "2 - Got a true expression value"  
    print var  
 elif var == 100:  
    print "3 - Got a true expression value"  
    print var  
 else:  
    print "4 - Got a false expression value"  
    print var  

print "Good bye!"
# try/except  
astr=input("Please enter a num: ")  
try:  
    istr=int(astr)  
    print("Your number is: ",astr)  
except:  
    istr=("0")  
    print("Incorrect type: ",istr)  
    print("You entered: ",astr,"- not a numer!")  
