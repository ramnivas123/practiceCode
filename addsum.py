

input1 = input("enter first number:")

while False == input1.isnumeric():
  input1 = input(" You have entered in correct value, please enter correct first number:")
          
num1 = float(input1)
if input1.isnumeric():
    num1 = float(input1)    

input2 = input("enter second number:")
while False == input2.isnumeric():
  input2 = input(" You have entered in correct value, please enter correct first number:")
      
num2 = float(input2)
if input1.isnumeric():
    num1 = float(input)   

sumOfNumbers = num1 + num2
 
print("the sum of given input number is = ", sumOfNumbers)