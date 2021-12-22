def show(user):
    print(f"имя: {user['имя']}")
    print(f"деньги: {user['деньги']}")
    print(f"жизни: {user['жизни']}")
    print(f"удача: {user['удача']}")
    user_inventory = user['инвентарь']
    for item in user_inventory:
        print(" •", item)
    print("")
