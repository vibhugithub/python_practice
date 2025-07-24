'''
generator function to generate Fibonacci numbers up to n.
This function uses a generator to yield Fibonacci numbers one by one.
'''


def fibonacci(n):
    a,b=0,1
    for i in range(n):
        yield a
        a,b = b,a+b
        
fib = fibonacci(10)
for i in fib:
    print(i,end =" ")