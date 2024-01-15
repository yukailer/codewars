def square_digits(num):
    res=""
    for i in str(num):
      res=res+str(int(i)*int(i))
    return int(res)
