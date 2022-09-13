""" 
8. Write a python program to create a function that accepts a string and calculate the
number of upper case letters and lower case letters.
 """
def fun(st):
    A=0;C=0
    for i in st:
        if ord(i)>=65 and ord(i)<=90:
            A+=1
        else:
            C+=1 

    print("Number of upper case letters are:",A,"Number of lower case letters are:",C)
   
fun(input("Enter a string:"))

#====================================OUTPUT=====================================
# Enter a string:Subham
# Number of upper case letters are: 1 Number of lower case letters are: 5

              