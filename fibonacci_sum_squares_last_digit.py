def fibonacci_fast_doubling(n: int):
    if n == 0:
        return (0, 1)
    else:
        a, b = fibonacci_fast_doubling(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)


def fibonacci_sum_squares_last_digit(n):
    # Taking into consideration last digit repeats after Pisano Period
    n = n % 60

    if n <= 1:
        return n

    fibonacci_n, fibonacci_n_plus_1 = fibonacci_fast_doubling(n)

    return (fibonacci_n * fibonacci_n_plus_1) % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares_last_digit(n))
