x = 1
y = 1
while True:
    if x == 1 and y == 1:
        print('You can travel: (N)orth.')
        att = input('Direction: ')
        if att != 'n' and att != 'N':
            print('Not a valid direction!')
            att = input('Direction: ')
        y += 1
    if x== 1 and y == 2:
        print('You can travel: (N)orth or (E)ast or (S)outh.')
        att = input('Direction: ')
        if att == 'w' or att == 'W':
            print('Not a valid direction!')
            att = input('Direction: ')
        if att == 'n' or att == 'N':
            y += 1
        elif att == 'e' or att == 'E':
            x += 1
        else:
            y -= 1
    if x== 2 and y == 2:
        print('You can travel: (S)outh or (W)est.')
        att = input('Direction: ')
        if att != 'w' and att != 'W' and  att != 's' and att != 'S':
            print('Not a valid direction!')
            att = input('Direction: ')
        if att == 'w' or att == 'W':
            x -= 1
        else:
            y -= 1
    if x== 2 and y == 1:
        print('You can travel: (N)orth.')
        att = input('Direction: ')
        if att != 'n' and att != 'N':
            print('Not a valid direction!')
            att = input('Direction: ')
        y += 1
    if x== 1 and y == 3:
        print('You can travel: (E)ast or (S)outh.')
        att = input('Direction: ')
        if att != 'e' and att != 'E' and  att != 's' and att != 'S':
            print('Not a valid direction!')
            att = input('Direction: ')
        if att == 'e' or att == 'E':
            x += 1
        else:
            y -= 1
    if x== 2 and y == 3:
        print('You can travel: (E)ast or (W)est.')
        att = input('Direction: ')
        if att != 'e' and att != 'E' and  att != 'w' and att != 'W':
            print('Not a valid direction!')
            att = input('Direction: ')
        if att == 'e' or att == 'E':
            x += 1
        else:
            x -= 1
    if x== 3 and y == 3:
        print('You can travel: (S)outh or (W)est.')
        att = input('Direction: ')
        if att != 'w' and att != 'W' and  att != 's' and att != 'S':
            print('Not a valid direction!')
            att = input('Direction: ')
        if att == 'w' or att == 'W':
            x -= 1
        else:
            y -= 1
    if x== 3 and y == 2:
        print('You can travel: (N)orth or (S)outh.')
        att = input('Direction: ')
        if att != 'n' and att != 'N' and  att != 's' and att != 'S':
            print('Not a valid direction!')
            att = input('Direction: ')
        if att == 'n' or att == 'N':
            y += 1
        else:
            y -= 1
    if x == 3 and y == 1:
        print('Victory!')
        break

