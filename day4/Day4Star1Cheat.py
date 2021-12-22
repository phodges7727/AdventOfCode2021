from typing import NamedTuple

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
        board += (int(x) for x in line.split())
    else:
        print(board)
        all_boards.append(board)
        board = []

print(all_boards)

#bingo_numbers = [int(s) for s in first.split(',')]
