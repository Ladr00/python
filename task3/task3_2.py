print("Введите слово маленькими буквами:")
a = input()

gls = {'a', 'e', 'i', 'o', 'u'}
gls_f = 0
sgl = 0

for letter in a:
    if letter.isalpha():
        if letter in gls:
            gls_f += 1
        else:
            sgl += 1

if gls_f == 0 or sgl == 0:
    print(False)
else:
    print("Количество гласных букв:", gls_f)
    print("Количество согласных букв:", sgl)