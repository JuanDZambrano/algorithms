def gcd(a, b):
    if a == 0:
        return b

    residue = b % a
    return gcd(residue, a)


def lcm(a: int, b: int):
    return int(a * b / gcd(a, b))


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))
