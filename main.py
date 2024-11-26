x = int(input('Which system should I transfer to?\n1. to DEC\n2. to BIN\n'))
y = input('Enter number: ')

if x==1:
    print(int(y, 2))
else:
    y=int(y)
    print(bin(y))