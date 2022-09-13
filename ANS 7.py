""" 
7. Write a python program to access a function inside a function.

 """
def fun1(x):
    def fun2(y):
        s=x+y
        return s
    print( fun2(int(input("Enter 2nd number:")))        )
      
fun1(int(input("Enter 1st number:")))

#======================================OUTPUT===================================
""" 
Enter 1st number:90
Enter 2nd number:76
166
 """
   

