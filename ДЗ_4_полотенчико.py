owners_NR = {
    "Trip": {
        "location": "Russia",
        "sex": "Men",
        "model_pc/laptop": "Laptop",
        "ip": "130.255.034.13"
    },
    "Kerb": {
        "location": "Russia",
        "sex": "Men",
        "model_pc/laptop": "Laptop",
        "ip": "130.255.06642"
    },
    "Don": {
        "location": "Kazakstan",
        "sex": "Men",
        "model_pc/laptop": "PC",
        "ip": "160.255.023.101"
    }
}

#----------------
#  ЗАДАНИЕ № 1  |
#----------------
from sys import argv
print("----- 1. -----")
age1 = input("Введите имя человека ")
print (owners_NR[age1])
print ("\n")

#----------------
#  ЗАДАНИЕ № 2  |
#----------------

print("----- 2. -----")
age1 = input("Введите имя человека: ")
parametr1 = input("Введите имя параметра: ")
parametr1_1 = owners_NR[age1].pop(parametr1)
print ("Вывод: ", parametr1_1)
print ("\n")

#----------------
#  ЗАДАНИЕ № 3  |
#----------------

print("----- 3. -----")
age1 = input("Введите имя человека: ")
parametr1 = list(owners_NR[age1])
stroka_1 = ", ".join(parametr1)   # Вывод следующий :  location, sex, model_pc/laptop, ip
stroka_2 = (f"{stroka_1}")
parametr2 = input(f"Введите имя параметра ({stroka_1}):")
parametr1_1 = owners_NR[age1].pop(parametr2)
print ("Вывод: ", parametr1_1)
print ("\n")

#----------------
#  ЗАДАНИЕ № 4  |
#----------------

print("----- 3. -----")
age1 = input("Введите имя человека: ")
parametr1 = list(owners_NR[age1])
stroka_1 = ", ".join(parametr1)   # Вывод следующий :  location, sex, model_pc/laptop, ip
stroka_2 = (f"{stroka_1}")
parametr2 = input(f"Введите имя параметра ({stroka_1}):")
print (owners_NR[age1].get(parametr2, "Такого параметра нет"))


#----------------
#  ЗАДАНИЕ № 5  |
#----------------

print("----- 3. -----")
age1 = input("Введите имя человека: ")
parametr1 = list(owners_NR[age1])
stroka_1 = ", ".join(parametr1)   # Вывод следующий :  location, sex, model_pc/laptop, ip
stroka_2 = (f"{stroka_1}")
parametr2 = input(f"Введите имя параметра ({stroka_1}):")
parametr2 = parametr2.lower()
print (owners_NR[age1].get(parametr2, "Такого параметра нет"))
