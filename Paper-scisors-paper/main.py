rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

# Convert game images in list
game_images= [rock, paper, scissors]

# Ask user and conver String to inter
user_choise = int(input("Type 0 for rock, 1 for paper, 2 for scisors \n"))
print(game_images[user_choise])
# Ask computer for a random number between given range using the random library
computer_choise = random.randint(0, 2)
print(game_images[computer_choise])
# calcular quem ganhou

if user_choise == 0 and computer_choise == 1:
  print("You win!")
else:
  print("You lose!")










