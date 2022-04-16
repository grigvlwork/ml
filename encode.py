def encode(data):
    str = ''
    for d in data:
        if d >= 0:
            str += f'{bin(d)[2:]:0>5}'
        else:
            str += f'1{bin(-d)[2:]:0>4}'
    num1 = int(str[:60], 2)
    num2 = int(str[60:], 2)
    return num1, num2


e = encode([i for i in range(24)])
print(e[0], e[1])
