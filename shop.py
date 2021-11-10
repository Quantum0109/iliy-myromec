import os

user_name = "Алах"
user_money = 1000
user_inventory = []


def show_location_shop(user_name: str, user_money: int, user_inventory: list):
	is_shopping = True
	potion_prise = 100
	while is_shopping:
		os.system("cls")
		print(f"салам {user_name}")
		print(f"1 - купить зелье, оно стоит {potion_prise}")
		print ("2 - уйти")
		user_choise = ""
		while user_choise not in ("1", "2"):
			user_choise = input("Что будем делать")
		if user_choise == "1" and user_money >= potion_prise:
			user_money -= potion_prise
			print(f"{user_name} купили зедье")
		elif user_choise == "1" and user_money < potion_prise:
			print (f"{user_name} не хавтило денег")
		else:
			is_shopping = False
			input("Enter продолжить")



show_location_shop(user_name, user_money, user_inventory)