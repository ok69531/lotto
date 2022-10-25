import random


def extract_number(*num: list):
    '''
        num: want to include in extracted number
    '''
    try:
        number = set(num)
    except:
        number = set()
    
    while len(number) < 6:
        number.add(random.randint(1, 45))
    
    return sorted(list(number))

extract_number()
extract_number(*[1, 2])
