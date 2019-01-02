#Anshul Ramavath
#Pitt Project 1 Monty Hall 3 
import random
win = 0
rounds = int(input("How many rounds from 10 - 10000, do you want to run the game:"))
while rounds <= 9 or rounds >= 10001:
    print("Must enter a number between 10 and 10000")
    rounds = int(input("Please try again:"))
print()
switchstay = input("Should the player 'switch' or 'stay'?")
while switchstay != "switch" and switchstay != "stay":
    print("Must enter either 'switch' or 'stay'")
    switchstay = input("Please try again:")
for num  in range(0,rounds):
  car = random.randint(1,3)
  guess = random.randint(1,3)
  if switchstay == "stay":
    if guess == 1:
      guess = 1
    elif guess == 2:
      guess = 2
    elif guess == 3:
      guess = 3
    elif car == guess:
      win += 1
  elif switchstay == "switch":
    if car == 1 and guess == 1:
      guess = 3
    elif car == 2 and guess == 1:
      guess = 2
    elif car == 3 and guess == 1:
      guess = 3
    elif car == 1 and guess == 2:
      guess = 2
    elif car == 2 and guess == 2:
      guess = 1
    elif car == 3 and guess == 2:
      guess = 3
    elif car == 1 and guess == 3:
      guess = 1
    elif car == 2 and guess == 3:
      guess = 2
    elif car == 3 and guess == 3:
      guess = 2
  if car == guess:
    win += 1
percentage = win/rounds
percentage *= 100
print("The player won ",win,"/",rounds, " games (", format(percentage,'.2f'),"%)",sep = "")