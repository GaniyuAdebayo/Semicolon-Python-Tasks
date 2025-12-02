
player1 = input("Player 1: Choose Rock, Paper or Scissors: ")
player2 = input("Player 2: Choose Rock, Paper or Scissors: ")

if (player1 == "Rock" and player2 == "Rock") or (player1 == "Scissors" and player2 == "Scissors") or (player1 == "Paper" and player2 == "Paper"):
	print("Tie")
elif (player1 == "Rock" and player2 == "Scissors"):
	print("Player 1 wins")
elif (player2 == "Rock" and player1 == "Scissors"):
	print("Player 2 wins")
elif (player1 == "Scissors" and player2 == "Paper"):
	print("Player 1 wins")
elif (player2 == "Scissors" and player1 == "Paper"):
	print("Player 2 wins")
elif (player1 == "Paper" and player2 == "Rock"):
	print("Player 1 wins")
else:
	print("Player 2 wins")

	