import random


def play_dice(user_money: int) -> int :
	bet = int(input("Сколько поставить? "))
	if bet > user_money:
		play_dice(user_money)
	if bet <= 0 : 
		print("не может быть")
		play_dice(user_money)

	user_dice = random.randint(2, 12)
	casino_dice = random.randint(2, 12)
	print(f"Вы бросили кости, выпало {user_dice}")
	print(f"Казино кости, выпало {casino_dice}")
	if user_dice > casino_dice:
		print("Вы победили")
		user_money += bet
	elif user_dice < casino_dice:
		print("Вы проиграли")
		user_money -= bet
	else:
		print("Ничья")
	print("Теперь у вас", user_money, "денег")
	input("Нажмите ENTER чтобы выйти")
	return user_money


user_money = 5000
user_money = play_dice(user_money)
print(user_money)

