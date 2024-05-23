def create_phone_number(n):
    str_n = "".join(str(i) for i in n)
    return "(%s) %s-%s" % (str_n[:3], str_n[3:6], str_n[6:])

'''
### best solution ###
def create_phone_number(n):
	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

######

def create_phone_number(n):
    n = ''.join(map(str,n))
    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])
'''
