def last_indexof_max(numbers):
    # write the modified algorithm here
    index = max(x for x, y in enumerate(numbers) if y == max(numbers))
    return index
