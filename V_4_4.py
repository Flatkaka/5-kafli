# is_prime function definition goes here
    
num = int(input("Input an integer greater than 1: "))

# Call the function here and print out the appropriate message
def is_prime (x):
    t = True
    for n in range(2,x):
        if (x % n) == 0:
            t = False
    return t

prime = is_prime(num)
if prime:
    print(num, 'is a prime')
else:
    print(num, 'is not a prime ')