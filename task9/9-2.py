
list1 = input("Введите числа первого списка через пробел: ").split()

list2 = input("Введите числа второго списка через пробел: ").split()

numbers = set(list1) & set(list2)

# Вывод списков рядом
print("Первый список:", " ".join(list1))
print("Второй список:", " ".join(list2))
print("Общие числа:", " ".join(numbers))
