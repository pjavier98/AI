from board import *
from util import *
from random import randint

def game(board, isHuman):
  while True:
    score = board.evaluate_function()
    if score == 10 and isHuman:
        print('Human is the winner')
        break
    elif score == -10 and not isHuman:
        print('AI is the winner')
        break
    
    isHuman = not isHuman
    if board.isMovesLeft():
      if isHuman:
        print('Human turns')
        print('Enter the row and column: ', end='')
        row, column = input().split()
        row = int(row)
        column = int(column)
        # return
        board.update_field(row, column, True)
        
      else:
        print('AI turns')
        # Find and update the best row and column based on the board
        board.findBestMove()
        print('row: ', board.bestMoveRow)
        print('column: ', board.bestMoveColumn)
        board.update_field(-1, -1, False)
      print('\n', str(board))
    else:
      print('There was a draw')
      break

def main():
  print('###################################')
  print('# Welcome to the tic-tac-toe game #')
  print('###################################\n')

  row = randint(0, 2)
  column = randint(0, 2)

  board = Board()

  board.update_initial_state(row, column)
  
  # False -> IA start
  print(str(board))
  game(board, False)

main()