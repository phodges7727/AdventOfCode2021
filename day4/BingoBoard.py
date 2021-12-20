from array import *
board = []

class BingoBoard:
  def __init__(self, board):
    self.board = board

  def __str__(self):
    return [x for x in self.board]
