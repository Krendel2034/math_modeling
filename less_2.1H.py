a = int(input('введите коэффициент А '))
b = int(input('введите коэффициент В '))
c = int(input('Введите коэффициент С '))
d = (b**2)-(4*a*c)
if d>0:
    print((-b+(d**0.5))/2)
    print((-b-(d**0.5))/2)
elif d==0:
    print(-b/(2*a))
else:
    print('корней нет')
