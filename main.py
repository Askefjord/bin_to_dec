isStart = True
while isStart == True:
    try:
        x = int(input('Which system should I transfer to?\n'
            '1. to DEC\n'
            '2. to BIN\n'
            '0. Exit\n'))

        if x==1:
            y = input('Enter number: ')
            print(int(y, 2))
        elif x==2:
            y = input('Enter number: ')
            y=int(y)
            print(bin(y))
        elif x==0:
            isStart = False
            break
        else:
            print('Invalid number')
            break

    except ValueError:
        print('Error\n')
        break