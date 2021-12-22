def save(user):
    with open("save", "w", encoding="utf-8") as file:
        file.write(str(user['имя']) + ",")
        file.write(str(user['деньги']) + ",")
        file.write(str(user['жизни']) + ",")
        file.write(str(user['удача']) + ",")
        for item in user['инвентарь']:
            file.write(item + ",")

def load(user):
    with open("save", "r", encoding="utf-8") as file:
    	hero_list = file.read().split(",")
    	user['имя'] = hero_list[0]
    	user['деньги'] = int(hero_list[1])
    	user['жизни'] = int(hero_list[2]) 
    	user['удача'] = int(hero_list[3]) 
    	user['инвентарь'] = hero_list[4:-1:1]

    	print(hero_list)
    	input("++++")

