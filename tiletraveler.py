x = 1
y = 1
def travel (main):
    print('You can travel:', main + '.')
def direction ():
    att = input('Direction: ')
    return att
def invalid (att, main):
    for n in main:
        if n.isupper():
            if att == n.lower() or att == n:
                break
    else:
        print('Not a valid direction!')
        att = input('Direction: ')
    return att
def move (att,x,y):
    if att == 'n' or att == 'N':
        y += 1
    elif att == 's' or att == 'S':
        y -= 1
    elif att == 'e' or att == 'E':
        x += 1
    else:
        x -= 1
    return x,y
def leidir (x,y):
    if y == 1:
        main = '(N)orth'
    elif y == 2:
        if x == 1:
            main = '(N)orth or (E)ast or (S)outh'
        elif x == 2:
            main = '(S)outh or (W)est'
        else:
            main = '(N)orth or (S)outh'
    else:
        if x == 1:
            main = '(E)ast or (S)outh'
        elif x == 2:
            main = '(E)ast or (W)est'
        else:
            main = '(S)outh or (W)est'
    return main

while x < 4 and y < 4:
        main = leidir(x,y)
        travel(main)
        att = direction()
        att = invalid(att, main )
        x,y = move(att, x, y)
        if x == 3 and y == 1:
            print('Victory!')
            break