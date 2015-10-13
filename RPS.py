import random

def rps():
	player_choice = int(raw_input("Choose 1 for Rock, 2 for Paper, or 3 for Scissors: "))

	player_choice = assign(player_choice)

	comp_choice = random.randint(1,3)

	comp_choice = assign(comp_choice)

	player_wins = 0
	comp_wins = 0
	draws = 0

	print "You chose {}".format(player_choice)

	if player_choice == comp_choice:
		print("Wow! A tie!")
		draws += 1
	elif player_choice == "Rock" and comp_choice == "Paper":
		print("The computer chose {}.You Lose...".format(comp_choice))
		comp_wins += 1
	elif player_choice == "Rock" and comp_choice == "Scissors":
		print("The computer chose {}. You Win!!!!".format(comp_choice))
		player_wins += 1
	elif player_choice == "Paper" and comp_choice == "Rock":
		print("The computer chose {}. You Win!!!!".format(comp_choice))
		player_wins += 1
	elif player_choice == "Paper" and comp_choice == "Scissors":
		print("The computer chose {}.You Lose...".format(comp_choice))
		comp_wins += 1
	elif player_choice == "Scissors" and comp_choice == "Rock":
		print("The computer chose {}.You Lose...".format(comp_choice))
		comp_wins += 1
	elif player_choice == "Scissors" and comp_choice == "Paper":
		print("The computer chose {}. You Win!!!!".format(comp_choice))
		player_wins += 1

	score(player_wins, comp_wins, draws)

def assign(choice):
	if choice == 1:
		choice = "Rock"
	elif choice == 2:
		choice = "Paper"
	else:
		choice = "Scissors"

	return choice


def score(player_wins, comp_wins, draws):
	player_score = 0
	comp_score = 0
	draw_score = 0

	player_score = player_score + player_wins
	comp_score = comp_score + comp_wins
	draw_score = draw_score + draws

	return player_score
	return comp_score
	return draw_score


while True:
	rps()
	
	again = raw_input("Would you like to play again? ")

	if again == "Y" or "y":
		continue
	else:
		print player_score
		print comp_score
		print draw_score
		break

