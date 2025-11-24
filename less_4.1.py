import random
a = random.randint(0,100)
b = random.randint(0,100)
c = random.randint(0,100)
massive1 = [random.randint(0,100) for i in range(a)]
massive2 = [random.randint(0,100) for i in range(b)]
massive3 = [random.randint(0,100) for i in range(c)]
d = max(massive1)
e = max(massive2)
f = max(massive3)
j = max(d,e,f)
print("самый большой элемент среди массивов:", j)
r = sum(massive1)+sum(massive2)+sum(massive3)
print(r)