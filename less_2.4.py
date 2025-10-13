a = 1
b = 2
c = int(input('Введите количество чисел'))
print(a)
for i in range(c-1):
    print(a)
    c = a+b
    a = b
    b = c
   