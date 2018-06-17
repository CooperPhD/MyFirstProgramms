number = int(input())

# Вычисляем десятки
if number//10 <=3:
    print('X' * (number// 10 - 5), end='')
elif number//10 == 4:
    print('XL', end='')
elif number//10 <=8:
    print('L' + 'X' * (number// 10 - 5), end='')
elif number//10 == 9:
    print('XC', end='')

number = number % 10
# Вычисляем еденицы
if  0 < number <= 3:
    print('I' * number)
elif number == 4:
    print('IV')
elif number <=8:
    print('V' + 'I' * (number - 5))
elif number == 9:
    print('IX')
