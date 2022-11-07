import random

user_nyeres = 0
gep_nyeres = 0

options = ["kő", "papír", "olló"]

while True:
    user_input = input("Kérlek válassz a következők közük: : kő/papír/olló, a kilépéshez : q ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # ko: 0, papir: 1, ollo 2
    computer_pick = options[random_number]
    print("A számitógép választott: ", computer_pick + ".")

    if user_input == "kő" and computer_pick == "olló":
        print("Te nyertél!")
        user_nyeres += 1

    elif user_input == "papir" or user_input == "papír" and computer_pick == "kő":
        print("Te nyertél! ")
        user_nyeres += 1

    elif user_input == "olló" and computer_pick == "papír":
        print("Te nyertél! ")
        user_nyeres += 1

    else:
        print("Vesztettél! ")
        user_nyeres += 1

print("Te nyertél", user_nyeres, "alkalommal!")
print("A gép nyert", gep_nyeres, "Alkalommal")
print("Helloszia!")