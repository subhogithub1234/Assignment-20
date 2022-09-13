""" 
3. Write a python program to create a function that prints the even numbers from a
given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
 """
def fun1(l1):
    l2=[e for e in l1 if e%2==0]
    print("Even numbers of list is:",l2)

fun1(l1=[1, 2, 3, 4, 5, 6, 7, 8, 9])

#=========================================OUTPUT=================================

#Even numbers of list is: [2, 4, 6, 8]