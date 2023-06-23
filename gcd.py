def gcd(a, b):
    if a == 0:
        return b

    residue = b % a
    return gcd(residue, a)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
