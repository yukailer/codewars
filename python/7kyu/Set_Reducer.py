from itertools import groupby

def set_reducer(inp):
  conv=inp
  while len(conv)>1:
    conv=gr(conv)
  print(conv[0])
  return conv[0]

def gr(some):
  converted=[]
  for g in groupby(some):
       converted.append(len(list(g[1])))
  return converted
