def a_file():
    with open("27-A_2.txt", 'r') as f:
        return [int(row.strip()) for row in f][1:]


def b_file():
    with open("27-B_2.txt", 'r') as f:
        return [int(row.strip()) for row in f][1:]


def main(array):
    max_0, max_2, max_7, max_14 = 1, 1, 1, 1
    for num in array:
        if num % 14 == 0:
            max_14 = max(max_14, num)
        elif num % 7 == 0:
            max_7 = max(max_7, num)
        elif num % 2 == 0:
            max_2 = max(max_2, num)
        else:
            max_0 = max(max_0, num)
    return max(max_14 * max(max_0, max_2, max_7), max_7 * max_2)

if __name__ == "__main__":
    print(f"{main(a_file())}\n{main(b_file())}")