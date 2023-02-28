# https://inf-ege.sdamgia.ru/problem?id=36040


def get_data(file: str) -> list:
    with open(file, 'r') as f:
        return [row.strip().split(' ') for row in f][1:]


def main(file_data: list) -> int:
    filter_list = [max([int(num) for num in trio]) for trio in file_data]
    result = sum(filter_list)
    for _ in range(100):
        result = result - min(filter_list) if result % 109 == 0 else result
        return result


if __name__ == "__main__":
    print(f"{main(get_data('27_A.txt'))}\n{main(get_data('27_B.txt'))}")
