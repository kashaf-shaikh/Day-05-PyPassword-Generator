import random
print("Welcome!! to username generator.")
random_words = ["Shadow", "Dragon", "Tiger", "Storm", "Ghost"]

user_f_name = input("Enter your First Name :\n")
user_favourite_num = input("Enter your Favourite number:\n")
random_word = random.choice(random_words)

random_number = []
for i in range(3):
    random_number.append(random.randint(0,255))
random.shuffle(random_number)

user_name = ""
user_name += user_f_name
user_name +=random_word
user_name += str(random.choice(random_number))
user_name +=user_favourite_num

print(f"Your Username is :{user_name}")
