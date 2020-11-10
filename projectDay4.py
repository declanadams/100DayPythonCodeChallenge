import random


print("Welcome to Rock, Paper, Scissors game. See if you have some luck ")


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
gameImages = [rock, paper, scissors]

choiceUser = int(input("what do you pick? Type 0 for Rock, 1 for Paper and 2 for Scissors\n"))
print(gameImages[choiceUser])


choiceComp = random.randint(0, 2)
print(f"computer, your turn ")
print(gameImages[choiceComp])


if choiceUser >= 3 or choiceUser < 0 :
    print("you typed something wrong")  

elif choiceUser == 0 and choiceComp == 2:
    print("User Wins")

elif choiceComp == 0 and choiceUser ==2:
    print("Computer wins")

elif choiceComp > choiceUser:
    print("Computer Wins")

elif choiceUser > choiceComp:    
    print("user wins")

elif choiceComp == choiceUser:
    print("its a draw")    

  






