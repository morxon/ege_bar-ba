from time import time
from numba import jit


def a_file():
    with open("27989_A.txt", 'r') as f:
        return [int(row.strip()) for row in f][1:]


def b_file():
    with open("27989_B.txt", 'r') as f:
        return [int(row.strip()) for row in f][1:]


@jit()
def main(array):
    """
    too looooong
    """
    counter = 0
    for _ in range(len(array)):
        num_ = array.pop(0)
        for num in array:
            if num * num_ % 26 == 0:
                counter += 1
    return counter


if __name__ == "__main__":
    print(time())
    print(f"{main(a_file())}\n{main(b_file())}")
    print(time())