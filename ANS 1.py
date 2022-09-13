""" 
1. Write a python program to create a function that takes a list and returns a new list
with the original list's unique elements.

 """
def fun1(s1):
    d1=set(s1)
    s2=list(d1)
    return s2
x=int(input("How many number you want to be insert:"))
s1=[]
for i in range(x):
    t=int(input())
    s1.append(t)
print("Old list",s1)    
print("New list",fun1(s1))
#===================================OUTPUT===========================================
""" 
How many number you want to be insert:6
12
23
14
12
14
15
Old list [12, 23, 14, 12, 14, 15]
New list [12, 15, 14, 23]
 """