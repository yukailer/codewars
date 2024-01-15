def spin_words(sentence):
  res = [i for j in sentence.split() for i in (j, ' ')][:-1]
  spinned = ""
  for i in res:
    if len(i)<5:
      spinned = spinned + i
    else:
      spinned = spinned + i[::-1]
  return spinned
