import datetime
import sqlite3
connection = sqlite3.connect("tictactoe.db")

def check_mark(r, c):
  if(str(board[r][c]) == '-'):
    return True
  return False

def place_mark(r, c, p):
  if(turnCount % 2 == 0):
    board[r][c] = 'X'
  else:
    board[r][c] = 'O' 
    
def game_over():
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
  
def display_winner(w):
  if(w == 0):
    print("Player 1 wins!")
  elif(w == 1):
    print("Player 2 wins!")
  elif(w == 2):
    print("Game is a draw")
    
def error(e):
  if(e == 0):
    print("Invalid row. Please select a number between 0-2.")
  elif(e == 1):
    print("Invalid column. Please select a number between 0-2.")
  elif(e == 2):
    print("Invalid choice. Please mark again.")
  
board = [['-','-','-'],['-','-','-'],['-','-','-']]

def print_board():
  for i in range(3):
    print(board[i])

turnCount = 0
playing = True
winner = 2
gameNum = 0
while(playing):
  print("Printing board...")
  print_board()
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
  if(check_mark(int(row), int(col))):
    place_mark(int(row), int(col), turnCount)
    if(game_over()):
      playing = False;
      winner = turnCount%2
    turnCount+=1
    if(turnCount == 9):
      playing = False;
  else:
    error(2)
print_board()
display_winner(winner)

# cursor object
cursor = connection.cursor()
cursor.execute("INSERT INTO games VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (gameNum, winner, datetime.datetime.now(), board[0][0], board[0][1], board[0][2], board[1][0], board[1][1], board[1][2], board[2][0], board[2][1], board[2][2]))
    
cursor.execute("SELECT * FROM games")

# store all the fetched data in the ans variable
ans = cursor.fetchall()

for i in ans:
    print(i)  
connection.close
