import random
from art import logo

for x in range(10):
  random_number = random.randint(1,101)

def lvl_easy():
    #print(random_number)
    attempts = 10
    correct_number = True
    while correct_number:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess.: "))
        if guess < random_number:
            print("Too Low")
            attempts = attempts - 1
        elif guess > random_number:
            print("Too high")
            attempts = attempts - 1
        else: 
            print(f"You got it! The answer was {random_number}.")
            correct_number = False

def lvl_medium():
    #print(random_number)
    attempts = 7
    correct_number = True
    while correct_number:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess.: "))
        if guess < random_number:
            print("Too Low")
        elif guess > random_number:
            print("Too high")
        else: 
            print(f"You got it! The answer was {random_number}.")
            correct_number = False

def lvl_hard():
    #print(random_number)
    attempts = 5
    correct_number = True
    while correct_number:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess.: "))
        if guess < random_number:
            print("Too Low")
        elif guess > random_number:
            print("Too high")
        else: 
            print(f"You got it! The answer was {random_number}.")
            correct_number = False

#print(random_number)
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy', 'medium' or 'hard': ")
correct_answer = True
while correct_answer: 
    if level != "easy" or "medium" or "hard":
        print("That's not a level. Pick again")
    level = input("Choose a difficulty. Type 'easy', 'medium' or 'hard': ")
    if level.lower() == "easy":
        lvl_easy()
        correct_answer = False
    elif level.lower() == "medium":
        lvl_medium()
        correct_answer = False
    elif level.lower() == "hard":
        lvl_hard()
        correct_answer = False



