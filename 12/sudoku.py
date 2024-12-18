class Sudoku:

  def __init__(self, board):
    self.board = board

  def print_board(self):
    for i in range(4):
      if i == 2:
        print("---------")
      for j in range(4):
        print(str(self.board[i][j])+" ",end="")
        if j == 1:
          print("| ",end="")
      print()  

  def is_allowed(self, row, col, value):
    if self.board[row-1][col-1] != 0:
      return False
    qdr1 = []
    qdr2 = []
    qdr3 = []
    qdr4 = []
    for i in range(2):
      for j in range(2):
        qdr1.append(self.board[i][j])
        qdr2.append(self.board[i][j+2])
        qdr3.append(self.board[i+2][j])
        qdr4.append(self.board[i+2][j+2])
    if (value >= 0 and value <=4):
      for i in range(4):
        if self.board[i][col-1] == value:
          return False
      for i in self.board[row-1]:
        if i == value:
          return False
      if row <= 2 and col <= 2 and value not in qdr1:
        return True
      elif row <= 2 and col > 2 and value not in qdr2:
        return True
      elif row > 2 and col <= 2 and value not in qdr3:
        return True
      elif row > 2 and col > 2 and value not in qdr4:
        return True
      else: return False
    else:
      return False

  # helper method - is sudoku solved?
  def is_filled(self):
    pass

  # alternative to the above method - find the first empty cell if exists
  # useful for automatic solver
  def find_first_empty_cell(self):
    pass

  def get_dead_cell(self):
    pass

  def add_player_number(self,row,col,value):
    if self.is_allowed(row,col,value):
      self.board[row-1][col-1] = value
      self.print_board()
    else:
      print("Cannot place a number!")

  def play(self):
    self.print_board()
    solved = 0
    numbers = [1,2,3,4]
    while solved != 4:
      number = input("Insert row, column and value to write(separated by spaces) e.g. : 2 4 3: ")
      numbers_to_add = number.split()
      self.add_player_number(int(numbers_to_add[0]),int(numbers_to_add[1]),int(numbers_to_add[2]))
      solved = 0
      for i in range(4):
        used = []
        for j in self.board[i]:
          if j in used:
            solved = 0
            break
          elif j not in used and j in numbers:
            used.append(j)  
        if len(used) == 4:
           solved += 1
    print("Congrats, you won!!!")
        

  def solve_board(self):
    pass

if __name__ == "__main__":

  # Test 1. Let the user solve an "easy" sudoku
  sudoku1 = Sudoku(
   [[0, 2, 1, 0],
    [0, 4, 2, 3],
    [2, 3, 4, 0],
    [4, 0, 3, 2]]
  )
  sudoku1.play()

  # Test 2. Let the user solve a "very hard" sudoku
  sudoku2 = Sudoku(
   [[0, 0, 4, 0],
    [3, 0, 0, 0],
    [0, 0, 3, 1],
    [0, 3, 0, 4]]
  )


  # Test 3. Automatically solves a "very hard" sudoku
  sudoku3 = Sudoku(
   [[0, 0, 4, 0],
    [3, 0, 0, 0],
    [0, 0, 3, 1],
    [0, 3, 0, 4]]
  )
  sudoku3.solve_board()
