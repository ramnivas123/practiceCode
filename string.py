str = input("enter the string")
reverse = ""
length  = len(str) - 1
while length >= 0:
    reverse = reverse + str[length]
    length = length-1
print(reverse)
