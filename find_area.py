import math

x1 = float(input('Введите значение для x1: '))
y1 = float(input('Введите значение для y1: '))
x2 = float(input('Введите значение для x2: '))
y2 = float(input('Введите значение для y2: '))
x3 = float(input('Введите значение для x3: '))
y3 = float(input('Введите значение для y3: '))


def find_area(x1, y1, x2, y2, x3, y3):
    a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    c = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)

    triangle = math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2)

    if triangle == True:
        with open('truefalse.txt', 'w') as file:
            file.write('True')
    else:
        with open('truefalse.txt', 'w') as file:
            file.write('False')

    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))

    return area


area = find_area(x1, y1, x2, y2, x3, y3)

with open('area.txt', 'w', encoding="UTF-8") as file:
    file.write('Площадь треугольника: ' + str(area))

print('Площадь треугольника:', area)
