def is_triangle(a, b, c):
	return a > 0 and b > 0 and c > 0 and (a + b > c) and b + c > a and (c + a > b)

'''
### best solution  ###
def is_triangle(a, b, c):
    a, b, c = sorted([a, b, c])
    return a + b > c

'''
