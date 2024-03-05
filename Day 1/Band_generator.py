import random

# 1. Create a greeting for your program.

greet = print("Welcome to Band Generator\n")
# print("Hello ", greet, "!")

# 2. Ask the user for the city that they grew up in.

city_name = input("Name your City name :\n")
# print(City_name)

# Something extra to spice the simple project

random_city_letters = " ".join(random.sample(city_name, min(len(city_name), 3)))

# 3. Ask the user for the name of a pet.

pet_name = input("Name your fav pet name :\n")

random_pet_letters = " ".join(random.sample(pet_name, min(len(pet_name), 3)))

# 4. Combine the name of their city and pet and show them their band name.

random_combination = " ".join([random_city_letters, random_pet_letters])
# print(random_combination)

# 5. Make sure the input cursor shows on a new line:

print("Band_name is : ", random_combination)

# Solution: https://replit.com/@swatimeher10/band-name-generator-start#main.py
