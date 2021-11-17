import os

user_hp = 100
user_money = 200
user_name = "Влад"
user_xp = "0"
user_luck = 1
user_lvl = 0

def show_arena():
	print("Вы пришли на арену, за убийство вам дают опыт и деньги")
	print(f"1 - ударить")
	print(f"2 - блок(-2 хп)")
	print(f"3 - сбежать(-3 хп)")
	input("Выбирите вариант")
