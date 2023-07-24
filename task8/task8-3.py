import math

l = int(input('грузоподъемности лодки: '))

if not 1 <= l <= 10e6:
    print('Превышен вес')
    exit()

b = int(input('Введите количество рыбаков: '))

if not 1 <= b <= 100:
    print('Превышено максимальное количество рыбаков')
    exit()

weight_mass = []
common_weight = 0

for i in range(b):
    weight = int(input(f'Вес {i + 1} рыбака: '))

    if not 1 <= weight <= l:
        print('Превышен максимальный вес рыбака')
        exit()

    weight_mass.append(weight)
    common_weight += weight

print(f'Минимальное количество лодок для перевозки - {math.ceil(common_weight / l)}')