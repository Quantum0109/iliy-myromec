import random
import os
rnd = 0

print("Вы сидите за своим игровым пк")
print("1 - пойти в казино")
print("2 - пойти играть в CS:GO")

user_choice = ""
while user_choice not in ("1","2"):
	user_choise = input("Что выбрать? ")
def show_main_location():
	os.system('cls')
	print("Вы сидите за своим игровым пк")
	print("1 - пойти в казино")
	print("2 - пойти играть в CS:GO")

	user_choice = ""
	while user_choice not in ("1","2"):
		user_choise = input("Что выбрать? ")
	
	if user_choice == "1":
		show_casino_location()
	else:
		print("Жду")
		show_main_location()

def show_casino_location():
	print("Вы в казино")
	print("1 - пойти домой")
	print("2 - кинуть кости")
	user_choice = ""
	while user_choice not in ("1","2"):
		user_choice = input("Что выбрать? ")
	if user_choice == "1":
		show_main_location()
	else:
		rnd = random.randrange(1, 12 , 1)
		print(rnd)
		show_casino_location()
		input("нажмите Enter чтобы выйти")
