x = int(input("Enter the value of 'x': "))
a = 0
b = 1
sum = 0
count = 1
while(count <= x):
  count += 1
  a = b
  b = sum
  sum = a + b
  print(sum, end = " ")
  
print("Fibonacci Series: ", end = " ")