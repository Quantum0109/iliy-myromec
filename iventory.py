user_name = "Вася"
user_money = 0
user_hp = 100
user_xp = 0
user_level = 1
user_inventory = []


def show_inventory(user_inventory):
    for item in user_inventory:
        print(item)
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
    potion_prise = 500
    print("Вы в магазине, делайте свой выбор")
    print(f"Привет, {user_name}!")
    print(user_money)
    print("1 - купить зелье здоровья за 500")
    print("2 - перейти в инветарь")
    print("3 - выйти")

    user_choice = ""
    while user_choice not in ("1", "2", "3"):
        user_choice = input("введите номер варианта и нажмите Enter ")

        if user_choice == "1" and user_money >= potion_prise:
                print("Вы купили зелье здоровья")
                user_inventory.append("зелье здоровья")
        elif user_choice == "1" and user_money < potion_prise:
            print("не хватает денег")
        elif user_choice == "3":
            show_inventory
        else: 
            print("Вы вышли из магазина")


user_inventory.append("меч")
user_inventory.append("щит")
user_inventory.append("конь")

show_inventory(user_inventory)
