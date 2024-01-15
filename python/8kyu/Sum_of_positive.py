def positive_sum(arr):
    pos_arr=[]
    for i in arr:
        if i > 0:
            pos_arr.append(i)
    return sum(pos_arr)
