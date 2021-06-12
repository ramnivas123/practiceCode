i = int(input(" enter a number"))
x=i
rev=0
while i>0:
    rev = (rev*10)+i%10
    i = i//10
    
if(x == rev):
    print("number is palindrome")
else:
    print("number is not palindrome")
    
    # #
# #
# string=input(("Enter a string:"))
# if(string==string[::-1]):
      # print("The string is a palindrome")
# else:
      # print("Not a palindrome")      