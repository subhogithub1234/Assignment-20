""" 
10. Write a python program to create a function to check whether a string is an anagram
or not.
 """
def fun1(st1,st2):
     print("String is anagram." if sorted(st1)==sorted(st2) else "String is not anagram.")


fun1(input("Enter the 1st string:"),input("Enter the 2nd string:"))

#===================================OUTPUT================================
""" 
Enter the 1st string:heart
Enter the 2nd string:earth
String is anagram.

Enter the 1st string:show
Enter the 2nd string:shows
String is not anagram.
 """
