import datetime
import sqlite3
connection = sqlite3.connect("tictactoe.db")

#checks to see if a mark can be placed in a location
def check_mark(r, c, board):
  if(str(board[r][c]) == '-'):
    return True
  return False

#places a mark in the specified location
def place_mark(r, c, p, board, turnCount):
  if(turnCount % 2 == 0):
    board[r][c] = 'X'
  else:
    board[r][c] = 'O' 

#checks to see if any winning combinations have been achieved    
def game_over(board):
  win = False
  if(board[0][0] != '-' and board[0][0] == board[0][1] and board[0][1] == board[0][2]):
    win = True
  elif(board[1][0] != '-' and board[1][0] == board[1][1] and board[1][1] == board[1][2]):
    win = True
  elif(board[2][0] != '-' and board[2][0] == board[2][1] and board[2][1] == board[2][2]):
    win = True
  elif(board[0][0] != '-' and board[0][0] == board[1][0] and board[1][0] == board[2][0]):
    win = True
  elif(board[0][1] != '-' and board[0][1] == board[1][1] and board[1][1] == board[2][1]):
    win = True
  elif(board[0][2] != '-' and board[0][2] == board[1][2] and board[1][2] == board[2][2]):
    win = True
  elif(board[0][0] != '-' and board[0][0] == board[1][1] and board[1][1] == board[2][2]):
    win = True
  elif(board[0][2] != '-' and board[0][2] == board[1][1] and board[1][1] == board[2][0]):
    win = True
  return win

#displays the winner or draw if no winner  
def display_winner(w):
  if(w == 0):
    print("Player 1 wins!")
  elif(w == 1):
    print("Player 2 wins!")
  elif(w == 2):
    print("Game is a draw")

#outputs the proper error message    
def error(e):
  if(e == 0):
    print("Invalid row. Please select a number between 0-2.")
  elif(e == 1):
    print("Invalid column. Please select a number between 0-2.")
  elif(e == 2):
    print("Invalid choice. Please choose again.")

#creates a blank board
def create_board():  
  board = [['-','-','-'],['-','-','-'],['-','-','-']]
  return board

#prints the game board
def print_board(board):
  for i in range(3):
    print(board[i])

#unit testing functions
#test placing and checking marks
def test_check_and_place_mark(p):
  board = create_board()
  for i in range(3):
    for j in range(3):
      print(check_mark(i, j, board))
      place_mark(i, j, p, board, p)
      print(check_mark(i, j, board))
      print_board(board)
      
#test winning configurations      
def test_game_over(p):
  combinations = [[[0, 0], [0, 1], [0, 2]], [[1, 0], [1, 1], [1, 2]], [[2, 0], [2, 1], [2, 2]], [[0, 0], [1, 0], [2, 0]], [[0, 1], [1, 1], [2, 1]], [[0, 2], [1, 2], [2, 2]], [[0, 0], [1, 1], [2, 2]], [[0, 2], [1, 1], [2, 0]]]
  for i in range(8):
    board = create_board()
    for j in range(3):
      place_mark(combinations[i][j][0], combinations[i][j][1], p, board, p)
    print_board(board)
    print(game_over(board))
    display_winner(p)
    
#sql code to add database entry
def database_entry(g, w, board, r):
  cursor = connection.cursor()
  cursor.execute("INSERT INTO games VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (g, w, datetime.datetime.now(), board[0][0], board[0][1], board[0][2], board[1][0], board[1][1], board[1][2], board[2][0], board[2][1], board[2][2]))
  cursor.execute("SELECT * FROM games")
  if(r == 'n' or r == 'N'):
    #store all the fetched data in the ans variable
    ans = cursor.fetchall()
    for i in ans:
      print(i)  

#main portion of the game
def main_game():
  #variable for keeping track of the turn
  turnCount = 0
  #variable that returns true while the game is in process
  playing = True
  #variable that keeps track of the winner 0 for player 1, 1 for player 2, and 2 for a draw
  winner = 2
  #yet to be implemented functionality where it will get the number of total games played from the database and save each complete game with a unique game number
  gameNum = 0
  board = create_board() 
  while(playing):
    print_board(board)
    if(turnCount % 2 == 0):
      print("Player 1, make your move")
    else:
      print("Player 2, make your move") 
    row = input("Enter row num (0-2):")
    while(row != '0' and row != '1' and row != '2'):
      error(0)
      row = input("Enter row num (0-2):")
    col = input("Enter col num (0-2):")
    while(col != '0' and col != '1' and col != '2'):
      error(1)
      col = input("Enter col num (0-2):")
    if(check_mark(int(row), int(col), board)):
      place_mark(int(row), int(col), turnCount, board, turnCount)
      if(game_over(board)):
        playing = False;
        winner = turnCount%2
      turnCount+=1
      if(turnCount == 9):
        playing = False;
      if(playing == False):
        print_board(board)
        display_winner(winner) 
        replay = input("Play again? ")
        while(replay != 'y' and replay != 'Y' and replay != 'n' and replay !='n'):
          print(error(2));
          replay = input("Play again? ")
        database_entry(gameNum, winner, board, replay)
        gameNum+=1
        if(replay == 'y' or replay == 'Y'):
          board = create_board()
          turnCount=0
          winner=2
          playing = True
        
    else:
      error(2)
  
  
  
#test_game_over(1)
#test_check_and_place_mark(1)
main_game()

connection.close

