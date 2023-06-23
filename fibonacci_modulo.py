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


def pisanoPeriod(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current \
            = current, (previous + current) % m

        # A Pisano Period starts with 01
        if (previous == 0 and current == 1):
            return i + 1


def fibonacci_module(n: int, m: int):
    # Getting the period
    pisano_period = pisanoPeriod(m)

    # Taking mod of N with period lenght
    n = n % pisano_period

    if n <= 1:
        return n

    return fibonacci_fast_doubling(n)[0] % m


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_module(n, m))
