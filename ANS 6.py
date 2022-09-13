""" 
6. Write a python program to create a function and print a list where the values are
square of numbers between 1 and 30.

 """
def fun1(s1):
    
    s2=[i**2 for i in s1 ]
    return s2
s1=[]
x=int(input("How many numbers you enter in list:"))    
print("Inser the numbers:")
for i in range(x):
    t=int(input())
    s1.append(t)
print(s1)
print(fun1(s1))

#=====================================OUTPUT===================================
""" 
How many numbers you enter in list:6
Inser the numbers:
2
3
4
5
6
7
[2, 3, 4, 5, 6, 7]
[4, 9, 16, 25, 36, 49]
 """
