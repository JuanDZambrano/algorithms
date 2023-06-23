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


def fibonacci_last_digit(n):
    if n <= 1:
        return n

    return fibonacci_fast_doubling(n)[0] % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
