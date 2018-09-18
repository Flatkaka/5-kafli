# Your function definition goes here

user_input = input("Enter a string: ")

# Call the function 
def stafir (strengur):
    countupper = 0
    countlower = 0
    for x in strengur:
        if x.isupper():
            countupper += 1 
        elif x.islower():
            countlower += 1
    return (countupper,countlower)
upper, lower = stafir(user_input)

print("Upper case count: ", upper)
print("Lower case count: ", lower)