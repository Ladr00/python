N = int(input("Введите количество чисел: "))

if not 1 <= N <= 100000:
    print("Неверное значение N. Пожалуйста, введите число от 1 до 100000.")
    exit()
numb = []

for i in range(N):
    num = int(input(f"Введите число: {i + 1}: "))
    numb.append(num)

un_num = []

for num in numb:
    if num not in un_num:
        un_num.append(num)

print(f"уникальных: {un_num}")
print(f"уникальных результат: {len(un_num)}")
