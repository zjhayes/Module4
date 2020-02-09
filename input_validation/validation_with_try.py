
def average(number1, number2, number3):
    if number1 < 0:
        raise ValueError
    elif number2 < 0:
        raise ValueError
    elif number3 < 0:
        raise ValueError
    else:
        return (number1 + number2 + number3) / 3


def main():
    try:
        print(average(90, -76, 88))
    except ValueError:
        print("Invalid input, must be positive number.")


if __name__== "__main__":
    main()