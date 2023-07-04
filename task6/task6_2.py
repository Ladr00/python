print("Число A:")
a = int(input())
print("Число B:")
b = int(input())


c = []


for num in range(a, b + 1):
    if num % 2 == 0:
        c.append(num)


print("Четные числа на отрезке [", a,",", b, "]:", ' '.join(map(str, c)))
