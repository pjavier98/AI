def read_city():
  while True:
    try:
      number = int(input())
      if (number >= 1 and number <= 10):
        return number
    except:
      pass
    print("Invalid city, please choose again from [1-10]")

def read_files(path):
  fileDistances = open(path, 'r')

  inputFile = []
  for i in range(10):
      inputFile.append(list(map(int, fileDistances.readline().split())))
  
  fileDistances.close()
  return inputFile

def print_files(file):
  for i in file:
    print(i)

def print_best_way(solution):
  for state in solution:
    print(str(state))
    