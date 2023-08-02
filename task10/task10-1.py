pets = {}

n = int(input("Сколько питомцев вы хотите добавить? "))

for i in range(n):
    pet_name = input(f"Введите имя питомца {i + 1}: ")
    pet_vid = input("Введите вид питомца: ")
    pet_vozrast = int(input("Введите возраст питомца: "))
    owner_name = input("Введите имя владельца: ")

    pet_info = {
        "Вид питомца": pet_vid,
        "Возраст питомца": pet_vozrast,
        "Имя владельца": owner_name
    }

    pets[pet_name] = pet_info

for pet_name, pet_info in pets.items():
    vozrast_str = "год" if pet_info["Возраст питомца"] == 1 else "лет"
    print(f"Это {pet_info['Вид питомца']} по кличке \"{pet_name}\". Возраст питомца: {pet_info['Возраст питомца']} {vozrast_str}. Имя владельца: {pet_info['Имя владельца']}")
