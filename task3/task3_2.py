print("Введите слово маленькими буквами:")
a = input()

gls = {'a', 'e', 'i', 'o', 'u'}
gls_f = {gls_n: 0 for gls_n in gls}
sgl = 0

for letter in a:
    if letter in gls:
        gls_f[letter] += 1
    elif letter.isalpha():
        sgl += 1

word = sum(gls_f.values())

if word == 0 or sgl == 0:
    print(False)
else:
    print(f"Количество согласных: {sgl}")
    for gls_n, count in gls_f.items():
        print(f"Количество гласных '{gls_n}': {count}")
