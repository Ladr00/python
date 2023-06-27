print("Введите минимальную сумму инвестиций:")
a = int(input())
print("Введите сумму денег у Майкла:")
b = int(input())
print("Введите сумму денег у Ивана:")
c = int(input())

if b >= a and c >= a:
    print(2) 
elif b >= a and c < a:
    print("Mike")
elif b < a and c >= a:
    print("Ivan")
elif b + c >= a:
    print(1)
else:
    print(0)