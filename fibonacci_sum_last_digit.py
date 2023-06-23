def fibonacci_sum_last_digit(n: int):
    a, b = 0, 1
    result = 1
    if n <= 1:
        return n
    for _ in range(n - 1):
        a, b = b, (a + b) % 10
        result += b
        result = result % 10
    return result


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_last_digit(n))
