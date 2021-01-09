from random import randint

EASY_TURNS = 10
HARD_TURNS = 5





def check_guess( guess, answer, turns):
	"""checks answer against guess and returns number of turns remaining"""
	if guess > answer:
		print("Too high, guess again")
		return turns - 1

	elif guess < answer:
		print("too low, guess again")
		return turns -1 

	else:
		print(f"you guessed it, {answer}")




def set_dif():
	level = input("choose difficulty:  type easy or hard\n")

	if level == "easy":
		return EASY_TURNS
	else:
		return HARD_TURNS	







def game():
	
    
    print("Lets play a game")
    print("im thinking of a random number between 1 and 100 ")
    answer = randint(1, 100)


    turns = set_dif()
    


    user_guess = 0

    while user_guess != answer:

       print(f"You have {turns} left")

       user_guess = int(input("make a guess:"))

       turns = check_guess(user_guess, answer, turns)
       if turns == 0:
           print("you have lost , no turns left ")
           return

	   
      

	  
	     
	   



game()