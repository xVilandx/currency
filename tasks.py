# task 1

def split(values, number):
    return [values[i:i + number] for i in range(0, len(values), number)]


assert split([1, 2, 3, 4], 2) == [
    [1, 2],
    [3, 4],
]
assert split([1, 2, 3, 4, 5, 6], 2) == [
    [1, 2],
    [3, 4],
    [5, 6],
]
assert split([1, 2, 3, 4, 5, 6], 3) == [
    [1, 2, 3],
    [4, 5, 6],
]
assert split([1, 2, 3, 4, 5], 3) == [
    [1, 2, 3],
    [4, 5],
]
assert split([1, 2, 3, 4, 5], 2) == [
    [1, 2],
    [3, 4],
    [5, ],
]
assert split([1, 2, 3, 4, 5], 10) == [
    [1, 2, 3, 4, 5],
]
