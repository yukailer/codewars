def high_and_low(numbers):
  num_list=list(numbers.split())
  return str(max([int(i) for i in num_list])) + " " + str(min([int(i) for i in num_list]))
