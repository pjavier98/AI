def read_input(lower, upper):
  while True:
    try:
      number = int(input())
      if (number >= lower and number <= upper):
        return number
    except:
      pass
    print("Invalid input, please choose again from [" + str(lower) + "-" + str(upper) + "]")