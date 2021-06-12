# simple function calling

def our_method(a, b):
    if a > b:
        a = a + 1
        a = a + 2
        a = a + 3
        a = a + 3
        a = a + 3
        a = a + 3
        a = a + 3
        return a
    else:
        b = b + 1
        b = b + 2
        b = b + 3
        return b
    
x = our_method(2, 3)
print(x)

def our_method1(c, d):
    if c > d:
        pass
    else:
        pass

y = our_method1(10, 8)
print(y)
    
