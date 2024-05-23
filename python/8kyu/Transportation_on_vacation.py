def rental_car_cost(d):
    discount=0
    if d in range(3,7):
        discount=20
    if d > 6:
        discount=50
    return d*40-discount

'''
### best solution ###
def rental_car_cost(d):
  return d * 40 - (d > 2) * 20 - (d > 6) * 30
'''
