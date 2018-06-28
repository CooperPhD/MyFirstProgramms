nubmber = int(input())
total = ''
while nubmber: # пока number не равно 0
    total += str(nubmber%2)
    nubmber //=2 # nubmber = nubmber // 2
print(total[::-1]) # переворачиваем строку
print(type(hex(12321)))
