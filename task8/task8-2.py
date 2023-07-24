a = int(input('Введите количество чисел: '))

if not 1 <= a <= 100000:
    print('Значение должно быть в диапазоне от 1 до 100000')
    exit()

b = list(map(int, input(f'Введите {a} чисел через пробел: ').split()))

if len(b) > a:
    print(f'количество чисел не может быть больше {a}')
    exit()

c = []

for i in range(-1, len(b) - 1):
    c.append(b[i])


print(b)
print(c)