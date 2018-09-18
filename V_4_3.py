# The function definition goes here

num = int(input("Enter a number: "))

# You call the function here
def range (x):
    if x > 1 and x < 555:
        print(x, "is in range.")
    else:
        print(x, 'is outside the range!')
range(num)