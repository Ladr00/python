import collections

pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        }
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        }
    }
}

def update(ID):
    if ID in pets:
        pet_info = pets[ID]
        pet_name = list(pet_info.keys())[0]

        new_vid = input("Введите новый вид питомца: ")
        new_age = int(input("Введите новый возраст питомца: "))
        new_name = input("Введите новое имя владельца: ")

        pet_info[pet_name]["Вид питомца"] = new_vid
        pet_info[pet_name]["Возраст питомца"] = new_age
        pet_info[pet_name]["Имя владельца"] = new_name

        print(f"Информация о питомце с ID {ID} успешно обновлена.")
    else:
        print("Питомец с таким ID не найден.")

def create():
    last = collections.deque(pets, maxlen=1)[0] if pets else 0
    new_id = last + 1

    name = input("Введите имя питомца: ")

    pets[new_id] = {
        name: {
            "Вид питомца": "",
            "Возраст питомца": 0,
            "Имя владельца": ""
        }
    }
    print(f"Запись о питомце с ID {new_id} успешно создана.")

def delete(ID):
    if ID in pets:
        del pets[ID]
        print(f"Запись о питомце с ID {ID} успешно удалена.")
    else:
        print("Питомец с таким ID не найден.")

def get_pet(ID):
    if ID in pets:
        return pets[ID]
    return False

def get_suffix(age):
    if age % 10 == 1 and age != 11:
        return "год"
    elif 2 <= age % 10 <= 4 and (age < 10 or age > 20):
        return "года"
    else:
        return "лет"

def pets_list():
    for pet_id, pet_info in pets.items():
        pet_name = list(pet_info.keys())[0]
        pet_data = pet_info[pet_name]
        print(f"ID: {pet_id}, Имя: {pet_name}, Вид: {pet_data['Вид питомца']}, Возраст: {pet_data['Возраст питомца']} {get_suffix(pet_data['Возраст питомца'])}, Владелец: {pet_data['Имя владельца']}")

command = ""
while command != 'stop':
    command = input("Введите команду (create, read, update, delete, list, stop): ")

    if command == 'create':
        create()
    elif command == 'read':
        pet_id = int(input("Введите ID питомца: "))
        pet_info = get_pet(pet_id)
        if pet_info:
            pet_name = list(pet_info.keys())[0]
            pet_data = pet_info[pet_name]
            print(f"Это {pet_data['Вид питомца']} по кличке \"{pet_name}\". Возраст питомца: {pet_data['Возраст питомца']} {get_suffix(pet_data['Возраст питомца'])}. Имя владельца: {pet_data['Имя владельца']}")
        else:
            print("Питомец с таким ID не найден.")
    elif command == 'update':
         pet_id = int(input("Введите ID питомца для обновления: "))
         update(pet_id)
    elif command == 'delete':
         pet_id = int(input("Введите ID питомца для удаления: "))
         delete(pet_id)
    elif command == 'list':
        pets_list()
    elif command == 'stop':
        print("Программа завершена.")
    else:
        print("Неверная команда. Пожалуйста, введите корректную команду.")
