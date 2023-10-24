# import random


def mapper(x):  # (unit -> length = 1)
    return x / (abs(x) + 1)


# for i in random.sample(range(-10000, 10000), 10):
#     print(i, mapper(i))
