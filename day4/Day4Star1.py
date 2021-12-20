from array import *

class BingoBoard:
  def __init__(self, board):
    self.board = board

  def printRows(self):
      for row in self.board:
          print(row)

  def __str__(self):
    return [x for x in self.board]
    
my_file = open("Day4input1.txt")
my_input = my_file.read()
bingo_lines = my_input.splitlines()
#print(bingo_lines)

bingo_numbers = bingo_lines[0].split(',')
#print(bingo_numbers)

board = []
all_Boards = []
i=2
while(i<len(bingo_lines)):
    if (bingo_lines[i] != ''):
        line = " ".join(bingo_lines[i].split())
        board.append(line.split(' '))
        #print(board)
    else:
        all_Boards.append(BingoBoard(board))
        board.clear()
    i += 1

#print(bingo_boards)
for b in all_Boards:
    print("Board Game")
    b.printRows()




#[f(x) if condition else g(x) for x in sequence]