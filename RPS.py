import random

player_score = 0
comp_score = 0
draw_score = 0
Playing = True

def rps():
	"""Main Section of running the actual Rock,Paper, Scissors game"""
	#Initialize game, and express expected input
	player_choice = int(raw_input("Time to play RPS!!! Choose 1 for Rock, 2 for Paper, or 3 for Scissors: "))

	#Use assign function to ccheck and convert users choice to Rock, Paper, or Scissors 
	player_choice = assign(player_choice)

	#Initiate computer random selection 
	comp_choice = random.randint(1,3)

	#Convert computers choice to Rock, Paper, or Scissors
	comp_choice = assign(comp_choice)

	#Initialize variable for scoreboard
	player_wins = 0
	comp_wins = 0
	draws = 0

	#Evaluate selections to choose winner and add increment scoreboard
	print "You chose {}".format(player_choice)

	if player_choice == comp_choice:
		print("Wow! A tie!")
		score("draw")
	elif player_choice == "Rock" and comp_choice == "Paper":
		print("The computer chose {}.You Lose...".format(comp_choice))
		score("comp")
	elif player_choice == "Rock" and comp_choice == "Scissors":
		print("The computer chose {}. You Win!!!!".format(comp_choice))
		score("player")
	elif player_choice == "Paper" and comp_choice == "Rock":
		print("The computer chose {}. You Win!!!!".format(comp_choice))
		score("player")
	elif player_choice == "Paper" and comp_choice == "Scissors":
		print("The computer chose {}.You Lose...".format(comp_choice))
		score("comp")
	elif player_choice == "Scissors" and comp_choice == "Rock":
		print("The computer chose {}.You Lose...".format(comp_choice))
		score("comp")
	elif player_choice == "Scissors" and comp_choice == "Paper":
		print("The computer chose {}. You Win!!!!".format(comp_choice))
		score("player")


def assign(choice):
	"""Ensures player chose 1,2, or 3"""
	while True:
		if choice in (1,2,3):
			break
		else:
			choice = int(raw_input("C'mon Bro, that'n not an option! Please choose 1 for Rock, 2 for Paper or 3 for Scissors: "))

	#Converts selection to R, P, or S
	if choice == 1:
		choice = "Rock"
	elif choice == 2:
		choice = "Paper"
	else:
		choice = "Scissors"

	return choice


def score(winner):
	"""Function to keep score"""
	global player_score
	global comp_score
	global draw_score

	#Incriment correct scoreboard
	if winner == "draw":
		draw_score += 1
	elif winner == "player":
		player_score += 1
	elif winner == "comp":
		comp_score += 1


	return player_score
	return comp_score
	return draw_score


def again(n):
    """Function to Verify user input is valid""" 
    
    ### Ensures the input is valid and capitalizes for uniformity
    while True:
		n = n.upper()
		if n in ("Y", "YES", "N", "NO"):
			break
		else:
			n = (raw_input(str("Please enter [y/n]")))
			n = n.upper()

     
    return n


while True:
	rps()
	
	n = (raw_input(str("Would you like to play again? ")))
	x = str(again(n))
	
	#Allows the game to continue or end upon request
	if x in ("N", "NO"):
		print "Player won {} games!".format(player_score)
		print "Computer won {} games!".format(comp_score)
		print "Player and Computer tied {} games!".format(draw_score)
		break
	else:
		continue


