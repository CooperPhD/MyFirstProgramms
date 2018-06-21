#Дано число . Закончите фразу “На лугу пасется…” одним из 
#возможных продолжений: “n коров”, “n корова”, “n коровы”,
#правильно склоняя слово “корова”.
n = int(input())

units = n % 10

if units == 1:
    print(n, 'korova')
elif units <= 4:
    print(n, 'korovy')
elif units <= 9:
    print(n, 'korov')

