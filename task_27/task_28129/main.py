# https://inf-ege.sdamgia.ru/problem?id=28129


def read_txt(file_name: str) -> list:  # give file_name to func
    with open(file_name, 'r') as file:  # open file use file_name and init. file. method with "auto" close file
        return [int(row.strip()) for row in file]  # iter. file as rows row.strip() split \n and return file data


def find_pair(file_data: list) -> list:
    require_num = max([num for num in file_data if num % 7 == 0])  # our pair will be eligable if it will contain
    # at least one number that is % 7, collect all nums % 7 and choose max
    file_data.remove(require_num) # delete require_num from array
    top_20_nums = (sorted(file_data.copy()))[-20:][::-1]  # copy file_data, sort it, chose last max nums [-20:],
    # [::-1] reverse array from max to min
    remains_require_num = require_num % 160  # remains require num
    for num in top_20_nums:  # iter top_20 array
        if num % 160 != remains_require_num:  # if remains num % 160 not equal remains_require_num
            return sorted([require_num, num])  # return pair, sort from min to max
        # else skip num


if __name__ == "__main__":
    A_file, B_file = read_txt('28129_A.txt'), read_txt('28129_B.txt')  # file data
    A_pair, B_pair = find_pair(A_file), find_pair(B_file)  # get pairs
    print(A_pair, B_pair)

