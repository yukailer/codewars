def disemvowel(string_):
  res = ""
  vowels=["a","e","i","o","u","A","E","I","O","U"]
  for i in string_:
    if i not in vowels:
      res += i
  return res
