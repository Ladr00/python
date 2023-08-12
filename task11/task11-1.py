def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def factorial_n(n):
    result = []
    while n >= 1:
        result.append(factorial(n))
        n -= 1
    return result

number = 3
factorial_list = factorial_n(factorial(number))

print("Список факториалов числа", factorial(number), "в убывающем порядке:", factorial_list)
