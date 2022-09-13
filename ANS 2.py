""" 
2. Write a python program to create a function that takes a number as a parameter and
checks if the number is prime or not.

 """

def fun1(n):
    c=0
    for i in range(2,n):
        if n%i==0 :   
           
           break
        c=i
    if n==c+1:
        print("number is prime.")
    else:  
      print(n,"is not Prime number.")
fun1(int(input("Enter a number:")))

#=======================================OUTPUT==============================
""" 
Enter a number:13
13 is Prime number.

Enter a number:25
25 is not Prime number.
 """