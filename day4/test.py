#40 0 92 18 66
from array import *

class BingoBoard:
    def __init__(self, board):
        self.board = board

    def printRows(self):
        for row in self.board:
            print(row)

    def checkBoard(self,numbers):
        col = []
        for row in self.board:
            if(all(elem in numbers for elem in row)):
                return True
        for i in range(5):
            col.clear()
            for j in range(5):
                col.append(self.board[j][i])
            print("Col: ",col)
            if(all(elem in numbers for elem in col)):
                return True
        return False
        
    def getSum(self,numbers):
        sum = 0
        for row in self.board:
            for cell in row:
                if cell not in numbers:
                    sum += int(cell)
                    print("Cell: ", cell, " sum= ", sum) 
        return sum       

    def __str__(self):
        return [x for x in self.board]
    
b = BingoBoard([['48', '83', '84', '85', '3'],['98', '80', '50', '96', '91'],['18', '69', '44', '62', '15'],['20', '88', '12', '45', '28'],['8', '29', '0', '37', '27']])
numlist = ['28','27','15','91','3']
b.printRows()
print(b.checkBoard(numlist))


#result =  all(elem in list1  for elem in list2)