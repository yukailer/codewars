def digital_root(n):
    while len(str(n)) > 1:
        x = sum([int(i) for i in str(n)])
        n = x
    return n
