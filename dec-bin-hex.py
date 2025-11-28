def menu():

    choice = int(input('''What do you want to do?(1-6)\n
    1.Decimal -> Binary\n
    2.Decimal -> hexadecimal\n
    3.Binary -> Decimal\n
    4.Binary -> hexadecimal\n
    5.hexadecimal -> Binary\n
    6.hexadecimal -> Decimal'''))
    while choice < 1 or choice > 6:
        choice = int(input('''What do you want to do?(1-6)\n
            1.Decimal -> Binary\n
            2.Decimal -> hexadecimal\n
            3.Binary -> Decimal\n
            4.Binary -> hexadecimal\n
            5.hexadecimal -> Binary\n
            6.hexadecimal -> Decimal'''))
    if choice == 1:
        pass  # Dec - Bin
    if choice == 2:
        pass  # Dec - Hex
    if choice == 3:
        pass  # Bin - Dec
    if choice == 4:
        binary_hexadecimal()
    if choice == 5:
        hexadecimal_binary()
    if choice == 6:
        hexadecimal_Decimal()


def binary_hexadecimal():
    text = input('Enter a binary: ')
    hexadecimal = []
    while len(text) % 4 != 0:
        text = '0' + text
    print(text)
    
    for x in range(0, len(text), 4):
        hexadecimal.append((text[x:x+4])[::-1])
    print(hexadecimal, "*")
    
    for x in range(0, len(hexadecimal)):
        total = 0
        
        for y in range(4):
            total += int(hexadecimal[x][y]) * (2 ** y)
            print(int(hexadecimal[x][y]) * (2 ** y))
        hexadecimal[x] = total
    print(hexadecimal)
    for x in range(len(hexadecimal)):
        if int(hexadecimal[x]) == 10:
            hexadecimal[x] = 'A'
        elif int(hexadecimal[x]) == 11:
            hexadecimal[x] = 'B'
        elif int(hexadecimal[x]) == 12:
            hexadecimal[x] = 'C'
        elif int(hexadecimal[x]) == 13:
            hexadecimal[x] = 'D'
        elif int(hexadecimal[x]) == 14:
            hexadecimal[x] = 'E'
        elif int(hexadecimal[x]) == 15:
            hexadecimal[x] = 'F'
    print(hexadecimal)


def hexadecimal_binary():
    text = input('Enter a hexadecimal: ')  # AC7F
    binary = ''
    for x in range(len(text)):
        if text[x] == 'A':
            binary += '1010'
        elif text[x] == 'B':
            binary += '1011'
        elif text[x] == 'C':
            binary += '1100'
        elif text[x] == 'D':
            binary += '1101'
        elif text[x] == 'E':
            binary += '1110'
        elif text[x] == 'F':
            binary += '1111'
        else:
            num = int(text[x])
            binary_num = ''
            while num >= 1:
                binary_num += str(num % 2)
                num = num//2
            if len(binary_num) < 4:
                binary_num += '0'*(4 - len(binary_num))
            print(binary_num[::-1])
            binary += binary_num[::-1]
    print(binary)


def hexadecimal_Decimal():
    text = input('Enter a hexadecimal: ')  # AC7F
    binary = ''
    for x in range(len(text)):
        if text[x] == 'A':
            binary += '1010'
        elif text[x] == 'B':
            binary += '1011'
        elif text[x] == 'C':
            binary += '1100'
        elif text[x] == 'D':
            binary += '1101'
        elif text[x] == 'E':
            binary += '1110'
        elif text[x] == 'F':
            binary += '1111'
        else:
            num = int(text[x])
            binary_num = ''
            while num >= 1:
                binary_num += str(num % 2)
                num = num // 2
            if len(binary_num) < 4:
                binary_num += '0' * (4 - len(binary_num))
            binary += binary_num[::-1]
    decimal = 0
    binary = binary[::-1]
    for y in range(0,len(binary)):
        decimal += int(binary[y])*2**y
    print(decimal)

menu()
