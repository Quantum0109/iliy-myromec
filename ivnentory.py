import os

user_name = "Вася"
user_money = 1000
user_hp = 100
user_xp = 100
user_level = 1
user_inventory = []
user_skills = "торговля -10%"


def show_inventory(user_inventory):
        print("1 - открыть магазин")
        print("2 - уйти")

        user_choice = ""
        while user_choice not in ("1", "2"):
            user_choice = input("введите номер варианта и нажмите Enter ")
        if user_choice == "1":
            show_shop(user_name, user_money, user_inventory)
        else:
            print("Вы ушли домой")

def show_shop(user_name, user_money, user_inventory):
    is_busy = True
    while is_busy:
        os.system("cls")
        print(f"имя: {user_name}")
        print(f"деньги: {user_money}")
        print("инвентарь: ")
        for item in user_inventory:
            print(item)
        print("----------------")
        potion_prise = 500
        print("Вы в магазине, делайте свой выбор")
        print(f"Привет, {user_name}!")
        print(user_money)
        print(f"1 - купить зелье здоровья за {potion_prise}")
        print("2 - перейти в инветарь")
        print("3 - выйти")

        user_choice = ""
        while user_choice not in ("1", "2"):
            user_choice = input("введите номер варианта и нажмите Enter ")
            if user_choice == "1" and user_money >= potion_prise:
                    user_money -= potion_prise
                    user_inventory.append("зелье")
            elif user_money <= potion_prise:
                print(f"вам не хватает денег")
                input(print("ENTER"))
            else:
                is_busy = False
                show_inventory(user_inventory)
                print(f"вы ушли дмой")



user_inventory.append("меч")
user_inventory.append("щит")
user_inventory.append("конь")

show_inventory(user_inventory)

