num = int(input("enter the number:"))
sum = 0
value = 1

while (value <= num):
    sum = sum + value
    value = value + 1

print("The Sum of Natural Numbers from 1 to {0} =  {1}".format(num, sum))