from itertools import groupby
from tokens import *
class Code(object):

    def add(self):
        f=open('datafiles/add.txt')
        print (f.read())
    
    def difference(self):
        f=open('datafiles/sub.txt')
        print (f.read())

    def mul(self):
        f=open('datafiles/mul.txt')
        print (f.read())

    def div(self):
        f=open('datafiles/div.txt')
        print (f.read())
    def travlink(self):
         f=open('datafiles/traverse_linked_list.txt')
         print (f.read())
    def strplaindom(self):
        f=open('datafiles/strpalindrome.txt')
        print(f.read())
    def numplaindom(self):
        f=open('datafiles/numpalindrome.txt')
        print(f.read())
    def percentage(self):
        f=open('datafiles/percentage.txt')
        print(f.read())
    def remainder(self):
        f=open('datafiles/remainder.txt')
        print (f.read())
    def divisor(self):
        f=open('datafiles/divisior.txt')
        print (f.read())
    def armstrong(self):
        f=open('datafiles/armstrong.txt')
        print (f.read())
c = Code()

s = a
#addition
if "sum" in s:
    c.add()
    l=[int(''.join(i)) for is_digit, i in groupby(s, str.isdigit) if is_digit]
    print (l[0]+l[1])
elif "ad" in s:
    c.add()
elif "add" in s:
    c.add()
elif "summat" in s:
    c.add()
#subtraction   
elif "difference" in s:
    c.difference()
    l=[int(''.join(i)) for is_digit, i in groupby(s, str.isdigit) if is_digit]
    print (l[0]-l[1])
elif "subtract" in s:
    c.difference()
#multiplication    
elif "multiplication" in s:
    c.mul()
    l=[int(''.join(i)) for is_digit, i in groupby(s, str.isdigit) if is_digit]
    print (l[0]*l[1])
elif "multipli" in s:
    c.mul()
elif "multipl" in s:
    c.mul()      
#division    
elif "divid" in s:
    c.div()
    l=[int(''.join(i)) for is_digit, i in groupby(s, str.isdigit) if is_digit]
    print (l[0]/l[1])
elif "divis" in s:
    c.div()
#linked_list
elif "travers" and "link" and "list" in s:
    c.travlink()
#palindrome
elif "string" and  "palindrom" in s:
    c.strplaindom()
elif "number" and  "palindrom" in s:
    c.numplaindom()
#percentage
elif "percentag" in s:
    c.percentage()
#remainder modulus
elif "remaind" in s:
    c.remainder()
#divisior
elif "divisor" in s:
    c.divisor()
#armstrong
elif "armstrong" in s:
    c.armstrong()
else:
    print("not yet ready ")
