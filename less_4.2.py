name = "IlyaSukhanov"
upper_str = ''.join([char + '_' for char in name]).upper()
ascii_upper = [ord(char) for char in upper_str]
lower_str = ''.join([char + '_' for char in name]).lower()
ascii_lower = [ord(char) for char in lower_str]
max_upper = max(ascii_upper)
min_upper = min(ascii_upper)
max_lower = max(ascii_lower)
min_lower = min(ascii_lower)
print("Строка в верхнем регистре:", upper_str)
print("ASCII коды (верхний регистр):", ascii_upper)
print("Строка в нижнем регистре:", lower_str)
print("ASCII коды (нижний регистр):", ascii_lower)
print("Наибольшее значение из верхнего регистра:", max(ascii_upper))
print("Наименьшее значение из верхнего регистра:", min(ascii_upper))
print("Наибольшее значение из нижнего регистра:", max(ascii_lower))
print("Наименьшее значение из нижнего регистра:", min(ascii_lower))