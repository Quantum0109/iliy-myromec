import os
import random


user_name = "Вася"
user_money = 5000



def show_location_home():
    # описываем место
    os.system("cls")
    print("Вы дома")
    print("1 - в казино")
    print("2 - ждать")

    # спросить пользователя
    user_choice = ""
    while user_choice not in ("1", "2"):
        user_choice = input("введите номер варианта и нажмите Enter ")

    # проверить ответ пользователя
    if user_choice == "1":
        show_location_casino()
    else:
        print("жду")
        os.system("cls")
        show_location_home()


def show_location_casino():
    # описываем место
    os.system("cls")
    print("Вы в казино")
    print("1 - домой")
    print("2 - ждать")
    print("3 - сыграть")

    # спросить пользователя
    user_choice = ""
    while user_choice not in ("1", "2", "3"):
        user_choice = input("введите номер варианта и нажмите Enter ")

    # проверить ответ пользователя
    if user_choice == "1":
        show_location_home()
    elif user_choice == "2":
        print("жду")
        os.system("cls")
        show_location_casino()
    else:
        show_gamble()


def show_gamble():
    global user_money
    user_dice = random.randint(2, 12)
    casino_dice = random.randint(2, 12)
    print(f"Вы бросили кости, выпало {user_dice}")
    print(f"Казино кости, выпало {casino_dice}")
    if user_dice > casino_dice:
        user_money += 100
        print("Вы победили")
        print(user_money)
    elif user_dice < casino_dice:
        user_money -= 200
        print("Вы проиграли")
        print(user_money)
    else:
        print("Ничья")
        user_money -= 100
        print(user_money)
    input("Нажмите ENTER чтобы вернуться в казино")
    show_location_casino()

    show_location_home()




show_location_home()
