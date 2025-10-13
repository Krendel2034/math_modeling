a, b = map(int,input().split())
if b == 0:
    print('Делитель равен 0')
elif a%b == 0:
    print(f'Делится. Частное: {a//b}')
else:
    print(f'Не делится. Частное: {a//b}, Остаток: {a%b}')
    