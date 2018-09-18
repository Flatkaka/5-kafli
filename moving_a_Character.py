tala = int(input('Input a position between 1 and 10: '))
a = 1
b = 10
def texti ():
    print('l - for moving left')
    print('r - for moving right')
    print('Any other letter for quitting')
    x = input('Input your choice: ')
    return x
def move (x,breyta):
    if x == 'r' and breyta != b:
        breyta += 1
    elif x == 'l' and breyta != a:
        breyta -= 1
    print('New position is:', breyta)
    return breyta
while True:
    x = texti()
    if x == 'r' or x == 'l':
        tala = move(x, tala)
    else:
        tala = move(x, tala)
        break
