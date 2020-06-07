def range_sum(numbers, a, b):
    result = 0

    for i in numbers:
        if i in range(a, (b + 1)):
            result += i

    return result


numbers = [int(i) for i in input().split()]
a, b = [int(i) for i in input().split()]  # input().split() # ...

print(range_sum(numbers, a, b))
