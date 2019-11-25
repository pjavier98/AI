from board import *

def read_input(lower, upper):
  while True:
    try:
      number = int(input())
      if (number >= lower and number <= upper):
        return number
    except:
      pass
    print("Invalid input, please choose again from [" + str(lower) + "-" + str(upper) + "]")


def game(turn):
  while True:
    if (human):

    else:

def main():
  print('###################################')
  print('# Welcome to the tic-tac-toe game #')
  print('###################################\n')

  print('select [1] for Artificial Intelligence to start')
  print('select [2] to you start')
  choose = read_input(1, 2)

  board = Board()

  # turn = 0
  # choose == 1 ? turn 
  game(1)

main()