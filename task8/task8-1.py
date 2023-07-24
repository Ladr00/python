a = int(input('Введите количество чисел: '))
res = []

if not 1 <= a <= 100000:
    print('Значение должно быть в диапазоне от 1 до 100000')
    exit()

for i in range(a):
    num = int(input(f'Введите число для индекса {i}: '))

    if num > 10e5:
        print('Число не должно быть больше 1000000')
        exit()

    res.append(num)

res.reverse()
print(*res)