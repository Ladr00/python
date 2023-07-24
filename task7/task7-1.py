def palid(s):
    return s == s[::-1]

a = input("Введите строку без пробелов: ")
if palid(a):
    print("yes")
else:
    print("no")
