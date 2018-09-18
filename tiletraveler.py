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

while True:
    if x == 1 and y == 1:
        main = '(N)orth'
        travel(main)
        att = direction()
        att = invalid(att, main )
        x,y = move(att, x, y)
    if x== 1 and y == 2:
        main = '(N)orth or (E)ast or (S)outh'
        travel(main)
        att = direction()
        att = invalid(att, main )
        x,y = move(att, x, y)
    if x== 2 and y == 2:
        main = '(S)outh or (W)est'
        travel(main)
        att = direction()
        att = invalid(att, main )
        x,y = move(att, x, y)
    if x== 2 and y == 1:
        main = '(N)orth'
        travel(main)
        att = direction()
        invalid(att, main )
        x,y = move(att, x, y)
    if x== 1 and y == 3:
        main = '(E)ast or (S)outh'
        travel(main)
        att = direction()
        att = invalid(att, main )
        x,y = move(att, x, y)
    if x== 2 and y == 3:
        main = '(E)ast or (W)est'
        travel(main)
        att = direction()
        att = invalid(att, main )
        x,y = move(att, x, y)
    if x== 3 and y == 3:
        main = '(S)outh or (W)est'
        travel(main)
        att = direction()
        att = invalid(att, main )
        x,y = move(att, x, y)
    if x== 3 and y == 2:
        main = '(N)orth or (S)outh'
        travel(main)
        att = direction()
        att = invalid(att, main )
        x,y = move(att, x, y)
    if x == 3 and y == 1:
        print('Victory!')
        break