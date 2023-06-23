def fibonacci_partial_sum_last_digit(m: int, n: int):
    # The last digit pattern repeats with a period of 60 (Pisano Period)
    m = m % 60
    n = n % 60
    if n < m:
        n += 60

    current = 0
    next = 1
    result = 0

    for i in range(n + 1):
        if i >= m:
            result += current

        new_current = next
        next = next + current
        current = new_current

    return result % 10


if __name__ == '__main__':
    m, n = map(int, input().split())
    print(fibonacci_partial_sum_last_digit(m, n))
