def pyramid_sum(lower: int, upper: int, margin: int = 0) -> int:
    """
    Get a lower and upper int value,
    then print a pyramidal figure of their sums.
    """
    blanks = " " * margin
    print(blanks, lower, upper)
    if lower > upper:
        print(blanks, 0)
        return 0
    else:
        result = lower + pyramid_sum(lower + 1, upper, margin + 4)
        print(blanks, result)
        return result

def run():
    number = pyramid_sum(1, 5)
    print(number)

if __name__ == "__main__":
    run()