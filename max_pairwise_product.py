def max_pairwise_product(numbers: list):
    if len(numbers) > 1:
        numbers.sort(reverse=True)
        max_product = numbers[0] * numbers[1]
    else: 
        max_product = 0

    return max_product


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
