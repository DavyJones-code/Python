a = float(input('Начальный результат: '))
b = float(input('конечный результат: '))
day = 0
while a < b:
    a = a + a / 10
    day += 1
print(day)

