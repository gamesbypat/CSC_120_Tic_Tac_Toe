def check_mark(r, c):
  if(str(board[r][c]) == '-'):
    return True
  return False

def place_mark(r, c, p):
  if(turnCount % 2 == 0):
    board[r][c] = 'X'
  else:
    board[r][c] = 'O' 
  
def error(e):
  if(e == 0):
    print("Invalid row. Please select a number between 0-2.")
  elif(e == 1):
    print("Invalid column. Please select a number between 0-2.")
  elif(e == 2):
    print("Invalid choice. Please mark again.")
  
board = [['-','-','-'],['-','-','-'],['-','-','-']]
turnCount = 0
playing = True
while(playing):
  print("Printing board...")
  for i in range(3):
    print(board[i])
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
    turnCount+=1
  else:
    error(2)
    
  

