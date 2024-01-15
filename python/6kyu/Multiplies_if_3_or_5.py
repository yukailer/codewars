def solution(number):
  res=0
  if number <= 0:
    return 0
  else:
    for i in range(number):
      if i % 5 == 0 or i % 3 == 0:
        res = res + i
  return res
