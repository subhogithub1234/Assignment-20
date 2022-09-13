""" 
9. Write a python program to create a function to check whether a string is a pangram
or not.

 """
def fun1(st):
    ap="abcdefghijklmnopurstuvwxyz"
    print("string is panagram." if sorted(st)==sorted(ap) else "string is not panagram.")

fun1(input("Enter a string"))   