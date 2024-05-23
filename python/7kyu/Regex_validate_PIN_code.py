def validate_pin(pin):
    return pin.isdigit() if len(pin)==4 or len(pin)==6 else False

'''
best solution

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()
'''
