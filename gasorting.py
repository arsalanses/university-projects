import random

user_list = random.sample(list(range(100)), 50)

target = sorted(user_list)

print(target)
