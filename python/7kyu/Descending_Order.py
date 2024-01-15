def descending_order(num):
    list_num = [i for i in str(num)]
    list_num.sort(reverse=True)
    return int(''.join(list_num))
