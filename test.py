nums = range(101)

"""
    на 3 - fizz
    на 5 - bazz
    на 3 и 5 - fizzbazz
    остальные как есть
"""

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbazz")
    elif i % 5 == 0:
        print("bazz")
    elif i % 3 == 0:
        print("fizz")
    else: 
        print(i)