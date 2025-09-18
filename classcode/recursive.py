def factorial(n, level=0):
    if not isinstance(n, int):
        print("Error: this only works with nonnegative integers")
        return
    if n < 0:
        print("Error: this only works with nonnegative integers")
        return
    if n == 0:
        result  = 1        # base case
    else:
        result = n * factorial(n-1, level+1)
    
    space = ' ' * level
    print(str(n) + ' ' + space + str(result))
    return result     
    
    
factorial("hello")
factorial(-5)
factorial(5)

def fibonacci(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    f1 = fibonacci(n-1)
    f2 = fibonacci(n-2)
    return f1 + f2

# fibonacci(1.5)