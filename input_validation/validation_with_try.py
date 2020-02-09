
def average(number1, number2, number3):
    average = (number1 + number2 + number3) / 3
    if average < 0:
        raise ValueError('Cannot average negative numbers.')
    return average