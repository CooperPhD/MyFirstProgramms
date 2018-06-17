number = int(input())
i = number%10
x = number//10

# Вычисляем десятки
if x <=3:
    print('X' * (x - 5), end='')
elif x == 4:
    print('XL', end='')
elif x <=8:
    print('L' + 'X' * (x - 5), end='')
elif x == 9:
    print('XC', end='')

# Вычисляем еденицы
if  0 < i <= 3:
    print('I' * i)
elif i == 4:
    print('IV')
elif i <=8:
    print('V' + 'I' * (i - 5))
elif i == 9:
    print('IX')
