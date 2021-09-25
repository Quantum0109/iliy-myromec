import random 

counter = 0
rnd = 0

while not rnd == 10000:
	rnd = random.randrange(10001)
	counter += 1
	if rnd == 10000:

		print(counter)
