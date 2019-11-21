def read_stations():
  while True:
    try:
      number = int(input())
      if (number >= 1 and number <= 14):
        return number
    except:
      pass
    print("Invalid station, please choose again from [1-14]")

def read_files(path):
  fileDistances = open(path, 'r')

  inputFile = []
  for i in range(14):
      inputFile.append(list(map(int, fileDistances.readline().split())))
  
  fileDistances.close()
  return inputFile

def print_files(file):
  for i in file:
    print(i)

def print_best_way(solution):
  # for state in solution:
  #   print(str(state))
  previous_cost = 0
  flag = 0
  for state in solution:
    if flag == 0:
      print('Station {}'.format(state.station), end='')
      flag = 1
    else:
      print(' >> {} km >> Station {}'.format((state.total_cost - previous_cost), state.station), end='')
      previous_cost = state.total_cost
  print('\nTotal Cost: {} km'.format(previous_cost))