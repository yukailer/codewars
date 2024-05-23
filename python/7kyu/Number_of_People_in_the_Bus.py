def number(bus_stops):
    x=0
    for a,b in bus_stops:
        x = x + a
        x = x - b
    return x

'''
### best solution ###
def number(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])
'''
