# find_min function definition goes here

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
    
# Call the function here
def find_min (first, second):
    if first > second:
        tala = second
    else:
        tala = first
    return tala
minimum = find_min(first, second)
print("Minimum: ", minimum)