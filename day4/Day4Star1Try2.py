
def checkBoard(cur_board,numbers):
        col = []
        for row in cur_board:
            #print(row)
            if(all(elem in numbers for elem in row)):
                print("row Found")
                return True
        for i in range(5):
            col.clear()
            for j in range(5):
                col.append(cur_board[j][i])
            #print("Col: ",col)
            if(all(elem in numbers for elem in col)):
                print("col Found")
                return True
        return False

my_file = open("Day4input1.txt")
my_input = my_file.read()
bingo_lines = my_input.splitlines()
#print(bingo_lines)
#['57','80','91','12','40'] +
bingo_numbers =  bingo_lines[0].split(',')
#print(bingo_numbers)

board = []
all_Boards = []
i=2
while(i<len(bingo_lines)):
    if (bingo_lines[i] != ''):
        row = [int(x) for x in bingo_lines[i].split()]
        board.append(row)
        #print(board)
    else:
        all_Boards.append(board)
        print(all_Boards)
        board.clear()
    i += 1



for i in range(len(all_Boards)):
    print("Board getting pulled from the list")
    print(all_Boards[i])

'''

win = False
i = 5
while(win != True):
    for b in all_Boards:
        if(checkBoard(b,bingo_numbers[0:i])):
            #b.printRows()
            winning_board = b
            break
        else:
            i += 1
    win = True


print("Numbers List")
print(bingo_numbers[0:i])
print("Winning Board")
print(winning_board)
            


'''
#[f(x) if condition else g(x) for x in sequence]