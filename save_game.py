def save(user_name, user_money, user_hp, user_luck, user_inventory, game):
    with open("save", "w", encoding="UTF-8") as file:
        file.write(str(user_name) + "\n")
        for item in user_inventory:
            file.write(str(item) + "\n")
        file.write(str(user_money) + "\n")
        file.write(str(user_hp) + "\n")
        file.write(str(user_luck) + "\n")
        file.write(str(game) + "\n")