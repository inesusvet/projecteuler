def gen_numbers():
    for num in range(1, 101)
        yield num


def square(number):
    return number ** 2


def main():
    sum_of_squares = sum(map(square, gen_numbers()))
    square_of_sum = square(sum(gen_numbers()))
    diff = abs(sum_of_squares - square_of_sum)
    return diff


if __name__ == '__main__':
    print main()
