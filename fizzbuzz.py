def react_to_nr(x):
    """
    Return "fizz" if the input number is divisible by 3, "buzz" if divisible by 5, "fizz buzz" if divisible by 15

    >>> react_to_nr(1)
    1
    >>> react_to_nr(3)
    'fizz'
    >>> react_to_nr(5)
    'buzz'
    >>> react_to_nr(15)
    'fizz buzz'
    """
    if x % 15 == 0:
        return "fizz buzz"
    elif x % 5 == 0:
        return "buzz"
    elif x % 3 == 0:
        return "fizz"
    else:
        return x


if __name__ == '__main__':
    # https://en.wikipedia.org/wiki/Fizz_buzz
    [print(react_to_nr(x)) for x in range(1, 21)]
