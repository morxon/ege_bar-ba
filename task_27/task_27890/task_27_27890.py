def a_file():
    with open("27-A_1 (2).txt", 'r') as f:
        return [row.split() for row in f][1:]


def b_file():
    with open("27-B_1 (2).txt", 'r') as f:
        return [row.split() for row in f][1:]


def min_sum(pairs):
    difference = 10**6
    summary = 0
    for pair in pairs:
        first, second = int(pair[0]), int(pair[1])
        summary += max(first, second)
        if abs(first - second) % 5 != 0:
            difference = min(difference, abs(first - second))
    if summary % 5 != 0:
        return summary
    else:
        return summary - difference


if __name__ == "__main__":
    print(f"{min_sum(a_file())}\n{min_sum(b_file())}")