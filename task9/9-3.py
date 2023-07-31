numbers = list(map(int, input("введите числа через пробел: ").split()))

seen_numbers = {}

for num in numbers:
    if num in seen_numbers:
        print(num, "YES")
    else:
        seen_numbers[num] = True
        print(num, "NO")