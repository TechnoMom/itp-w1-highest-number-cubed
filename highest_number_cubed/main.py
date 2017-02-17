"""This is the entry point of the program."""


def highest_number_cubed(limit):
    '''the highest number that can be cubed that's less than the limit'''
    previous_number = 1
    
    while True:
        current_number = previous_number + 1
        if current_number ** 3 > limit:
            return previous_number
            
        previous_number = current_number
    