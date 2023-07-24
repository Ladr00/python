def palid(s):
    return s == s[::-1]

a = input("Введите строку без пробелов: ")
if pali(a):
    print("yes")
else:
    print("no")