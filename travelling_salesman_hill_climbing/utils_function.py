def read_input(lower, upper):
  while True:
    try:
      number = int(input())
      if (number >= lower and number <= upper):
        return number
    except:
      pass
    print("Invalid input, please choose again from [" + str(lower) + "-" + str(upper) + "]")

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
    