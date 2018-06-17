first_last_name = str(input()) #вводим два слова
print(type(first_last_name.split())) #выводим список  
a, b = map(len, first_last_name.split()) #присваеваем
print(a, b)


