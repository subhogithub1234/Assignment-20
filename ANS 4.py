""" 
4. Write a python program to create a function that checks whether a passed string is
palindrome or not.
 """
def fun1(st):
    print("Palindrome" if st==st[::-1] else "Not Palindrome")
fun1(input("Enter the string:"))   

#==================================OUTPUT========================================
# Enter the string:madam
# Palindrome

# Enter the string:Sir   
# Not Palindrome