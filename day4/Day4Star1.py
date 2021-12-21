from array import *

class BingoBoard:
    def __init__(self, board, index):
        self.bingo_board = board
        self.boardnumber = index

    def printRows(self):
        for row in self.bingo_board:
            print(row)

    def checkBoard(self,numbers):
        col = []
        for row in self.bingo_board:
            #print(row)
            if(all(elem in numbers for elem in row)):
                return True
        for i in range(5):
            col.clear()
            for j in range(5):
                col.append(self.bingo_board[j][i])
            #print("Col: ",col)
            if(all(elem in numbers for elem in col)):
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
#print(bingo_lines)

bingo_numbers = ['40','0','66','92','18'] + bingo_lines[0].split(',')
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
        print("Board being put into the list")
        b =BingoBoard(board,i)
        all_Boards.append(b)
        b.printRows()
        board.clear()
    i += 1


print(all_Boards[3])
'''
for i in range(len(all_Boards)):
    print("Board getting pulled from the list")
    all_Boards[i].board


win = False
i = 5
while(win != True):
    for b in all_Boards:
        if(b.checkBoard(bingo_numbers[0:i])):
            #b.printRows()
            winning_board = b
            break
        else:
            i += 1
    win = True

print(bingo_numbers[0:i])
winning_board.printRows()

print(winning_board.getSum(bingo_numbers[0:i]))
print(bingo_numbers[i-1])  
print(int(bingo_numbers[i-1])*int(winning_board.getSum(bingo_numbers[0:i])))
            
for b in all_Boards:
    b.printRows()

'''

#[f(x) if condition else g(x) for x in sequence]