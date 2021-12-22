from array import *
import time

class BingoBoard:
    def __init__(self, board):
        self.bingo_board = board

    def printRows(self):
        for row in self.bingo_board:
            print(row)

    def checkBoard(self,numbers):
        col = []
        for row in self.bingo_board:
            #print(row)
            if(all(elem in numbers for elem in row)):
                #print("winning nums: ",numbers)
                #print("Winning board: ")
                #self.printRows()
                #print("Row win: ", row)
                return True
        for i in range(5):
            col = []
            for j in range(5):
                col.append(self.bingo_board[j][i])
            #print("Col: ",col)
            if(all(elem in numbers for elem in col)):
                #print("winning nums: ",numbers)
                #print("Winning board: ")
                #self.printRows()
                print("Col win: " ,col)
                return True
        return False

    
    def getSum(self,numbers):
        sum = 0
        for row in self.bingo_board:
            for cell in row:
                if cell not in numbers:
                    sum += int(cell)
        return sum       

    def __str__(self):
        print("Printing")
        self.printRows()
        return "This is a board" + str(self.boardnumber)
    
my_file = open("Day4input1.txt")
my_input = my_file.read()
bingo_lines = my_input.splitlines()
bingo_numbers = [int(x) for x in bingo_lines[0].split(',')]
bingo_lines.remove(bingo_lines[0])
bingo_lines.remove(bingo_lines[0])

all_boards = []
board = []
for line in bingo_lines:
    if(line != ''):
        row = [int(x) for x in line.split()]
        board.append(row)
    else:
        all_boards.append(BingoBoard(board))
        board = []




win = False
i = 0
while(win != True):
    for b in all_boards:
        if(b.checkBoard(bingo_numbers[0:i])):
            #b.printRows()
            winning_board = b
            break
        else:
            i += 1
    win = True

print(bingo_numbers[0:i])
winning_board.printRows()

'''
print(winning_board.getSum(bingo_numbers[0:i]))
print(bingo_numbers[i-1])  
print(int(bingo_numbers[i-1])*int(winning_board.getSum(bingo_numbers[0:i])))
            

'''

#[f(x) if condition else g(x) for x in sequence]