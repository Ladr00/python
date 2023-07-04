a = int(input())

if a == 1:
    b = 1
else:
    b = 2
    for i in range(2, int((a/2) + 1)):
        if a % i == 0:
            b += 1

print(b)