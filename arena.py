import os
import show_player
from random import choice


def show_location(user, game):
    # главный цикл модуля
    # заканчивается, если игрок выберет вернуться в лагерь
    is_busy = True
    while is_busy:
        # печатаем инфу о месте и игроке
        # предлагаем игроку выбор действий
        os.system("cls")
        show_player.show(user)
        print(f"{user['имя']} вошел на арену. Тут пока нечего делать.")
        print("1 — Сражаться")
        print("2 — Вернуться в лагерь")

        # игрок выбирает вариант
        user_choice = input("Что делать? ")

        # вариант: сражаемся
        if user_choice == "1":

            # создаем соперника
            enemy_first_names = ["Жран", "Дрын", "Рван"]
            enemy_second_names = ["Позорный", "Зловонный", "Чванливый"]
            enemy_name = choice(enemy_first_names) + " " + choice(enemy_second_names)
            enemy_hp = 100

            # цикл сражения
            is_fighting = True
            while is_fighting:
                os.system("cls")
                show_player.show(user)
                print(f"имя соперника: {enemy_name}")
                print(f"жизни соперника: {enemy_hp}")
                print("")
                print("1 - Атаковать")
                print("2 - Защищаться")
                if "зелье" in user['инвентарь']:
                    print("3 - Выпить зелье")
                user_choice = input("Что делать? ")

                if user_choice == "1":
                    enemy_hp -= 10
                    print(f"{enemy_name} ранен на 10 жизней")
                elif user_choice == "2":
                    user['жизни'] -= 10
                    print(f"{user['имя']} ранен на 10 жизней")
                elif user_choice == "3" and "зелье" in user['инвентарь']:
                    print(f"{user['имя']} выпил зелье и воостановил здоровье")
                    user['инвентарь'].remove("зелье")
                    user_hp = 100
                else:
                    print("Такого варианта нет, попробуйте другой.")

                input("ENTER — продолжить")

        # вариант: уходим в лагерь
        elif user_choice == "2":
            is_busy = False
            print(f"{user['имя']} отправился в лагерь.")

        # все остальные варианты
        else:
            print("Такого варианта нет, попробуйте другой.")

        input("ENTER — дальше")
