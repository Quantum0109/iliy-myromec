print ("Подъезжает Илья к трем дорожкам, на перекрестке камень лежит, а на том камне написано: «Кто вправо поедет - тому убитым быть, кто влево поедет - тому богатым быть, а кто прямо поедет - тому женатым быть».")
print (" 1 - Поеду-ка я по той дорожке, где убитому быть. Умру в чистом поле, как славный богатырь!")
print (" 2 - Ну, поеду теперь, где женатому быть!")
print (" 3 - Ну, поеду теперь в дорожку, где богатому быть.")
user_choice = ""

while user_choice not in ("1","2","3"):
	user_choice = input("Что выбрать? ")

if user_choice == "1":
	print("По первой")
	print("1 - хорошая концовка")
	print("2 - плохая концовка")
	user_choice = ""
	while user_choice not in ("1","2"):
		user_choice = input("Что выбрать? ")
	if user_choice == "1":
		print("Илья Муромец убил всех разбойников")
	elif user_choice == "2":
		print("У Ильи Муромца отжали все вещи и зажарили на костре")
	else:
		print("ERROR")

elif user_choice == "2":
	print("По второй")
	print("1 - хорошая концовка")
	print("2 - плохая концовка")
	user_choice = ""
	while user_choice not in ("1","2"):
		user_choice = input("Что выбрать? ")
	if user_choice == "1":
		print("Илья Муромец женился на прекрасной даме и жил счастливо ")
	elif user_choice == "2":
		print("Илью Муромца заставили женица на чудеще болоном и пошёл он на смертную казнь за убийчтво своей жены")
	else:
		print("ERROR")
elif user_choice == "3":
	print("По третьей")
	print("1 - хорошая концовка")
	print("2 - плохая концовка")
	user_choice = ""
	while user_choice not in ("1","2"):
		user_choice = input("Что выбрать? ")
	if user_choice == "1":
		print("Разбогател Илья Муромец и отдал всё в казну.")
	elif user_choice == "2":
		print("Илью Муромца обокрали и заставили выплачивать налоги.")
	else:
		print("ERROR")
else:
	print("Конец!")

