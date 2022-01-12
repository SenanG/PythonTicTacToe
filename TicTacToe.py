# Global Variables
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
gameGoingCheck = True 
winner = None
currentPlayer = "X"


#Calling Functions
#Play a game of tic tac toe
def play_game():

  #Displays the game board
  display_board()

  #Loop until the game stops 
  while gameGoingCheck:

    #Handle a turn
    handle_turn(currentPlayer)

    #Checks if game is over
    check_if_game_over()

    #Switches Player
    switch_player()
  
  #Prints winner or draw
  if winner == "X" or winner == "O":
    print(winner + " won.")
  elif winner == None:
    print("Tie.")


#Displays Game Board
def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")


# Handle a turn for any player
def handle_turn(player):

  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")

  valid = False
  while not valid:

    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")
 
    position = int(position) - 1

    if board[position] == "-":
      valid = True
    else:
      print("You can't go there. Go again.")

  # Put the game piece on the board
  board[position] = player

  # Show the game board
  display_board()


# Check if the game is over
def check_if_game_over():
  check_for_winner()
  check_for_tie()


# Check to see if somebody has won
def check_for_winner():
  global winner
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None


# Check the rows for a win
def check_rows():
  global gameGoingCheck
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  if row_1 or row_2 or row_3:
    gameGoingCheck = False
  if row_1:
    return board[0] 
  elif row_2:
    return board[3] 
  elif row_3:
    return board[6]
  else:
    return None


#Checks Columns for win
def check_columns():
  global gameGoingCheck
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  if column_1 or column_2 or column_3:
    gameGoingCheck = False
  if column_1:
    return board[0] 
  elif column_2:
    return board[1] 
  elif column_3:
    return board[2] 
  else:
    return None


#Checks Diagonals for win
def check_diagonals():
  global gameGoingCheck
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  if diagonal_1 or diagonal_2:
    gameGoingCheck = False
  if diagonal_1:
    return board[0] 
  elif diagonal_2:
    return board[2]
  else:
    return None


#Checks for a tie
def check_for_tie():
  global gameGoingCheck
  if "-" not in board:
    gameGoingCheck = False
    return True
  else:
    return False


#Switches Player
def switch_player():
  global currentPlayer
  if currentPlayer == "X":
    currentPlayer = "O"
  elif currentPlayer == "O":
    currentPlayer = "X"

#Plays game
play_game()