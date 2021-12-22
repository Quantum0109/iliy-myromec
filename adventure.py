import os
import show_player


def show_location(user, game):
    # главный цикл модуля
    # заканчивается, если игрок выберет вернуться в лагерь
    is_busy = True
    while is_busy:
        # печатаем инфу о месте и игроке
        # предлагаем игроку выбор действий
        os.system("cls")
        show_player.show(user)
        print(f"{user['имя']} выбрался из лагеря в окрестности. Тут пока нечего делать.")
        print("1 — Поискать приключения")
        print("2 — Вернуться в лагерь")

        # игрок выбирает вариант
        user_choice = input("Что делать? ")

        # вариант: ищем приключения
        if user_choice == "1":
            print(f"Пока что {user['имя']} не сможет найти тут приключений.")

        # вариант: уходим в лагерь
        elif user_choice == "2":
            is_busy = False
            print(f"{user['имя']} отправился в лагерь.")

        # все остальные варианты
        else:
            print("Такого варианта нет, попробуйте другой.")

        input("ENTER — дальше")