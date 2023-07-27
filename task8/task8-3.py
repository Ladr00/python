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

for i in range(b):
    weight_mass.append(int(input(f'{i + 1} рыбака: ')))
    weight_mass.sort()
bort, y, x = 0, 0, b -1

while y <= x:
    if y == x:
        bort += 1
        break
    if weight_mass[y] + weight_mass[x] <= l:
        y += 1
    x -= 1
    bort += 1

    
print(f'Минимальное количество лодок для перевозки - {bort}')
