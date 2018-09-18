# palindrome function definition goes here

in_str = input("Enter a string: ")

# call the function and print out the appropriate message
def strip (strengur):
    ord = ''
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for x in strengur:
        if x.isupper():
            x = x.lower()
            ord += x
        elif x.isspace():
            x = ''
            ord += x
        elif x in punctuations:
            x = ''
            ord += x
        else:
            ord += x
    return ord

def palindrome (ord):
    if ord == ord[::-1]:
        string = True
    else:
        string = False
    return string

ord = strip(in_str)
string = palindrome(ord)
if string:
    print('"'+ in_str + '"', 'is a palindrome.')
else:
    print('"'+ in_str + '"', 'is not a palindrome.')