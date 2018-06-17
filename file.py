number = int(input())
i = number%10 # еденицы
x = number//10 # десятки
roman = ''

# Вычисляем десятки
if x <=3:
    roman += 'X' * (x - 5)
elif x == 4:
    roman += 'XL'
elif x <=8:
    roman += 'L' + 'X' * (x - 5)
elif x == 9:
    roman += 'XC'

# Вычисляем еденицы
if  0 < i <= 3:
    roman += 'I' * i
elif i == 4:
    roman += 'IV'
elif i <=8:
    roman += 'V' + 'I' * (i - 5)
elif i == 9:
    roman += 'IX'

print(roman)