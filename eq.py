f = input() #уравнение формы ax+b=0
a = int(f[0]) # Число a
b = int(f[f.find('+')+1:f.find('=')]) # Число b
x = -b/a
print(x)
