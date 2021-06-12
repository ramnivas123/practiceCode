def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
input = int(input("enter the value"))
if input <= 0:
    print("enter a positive number")
else:
    print("fibonacci series:")
    for i in range(input):
        print(fibonacci(i))
print(fibonacci)