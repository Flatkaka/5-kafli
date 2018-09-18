# Your function definition goes here

n = int(input("Input the length of Fibonacci sequence (n>=1): "))
# Call your function here        
def fibonacci(tala):
    x1 = 1
    x2 = 1
    count = 0
    for n in range(1,tala+1):
        if n == 1:
            print(1, end=' ')
        elif n == 2:
            print(1, end=' ')
        else:
            x3 = x1 + x2
            x2 = x1
            x1 = x3
            print(x3, end=' ')
fibonacci(n)
