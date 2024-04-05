def read_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return lines


def find_common_and_different_lines(file1_lines, file2_lines):
    common_lines = set(file1_lines) & set(file2_lines)
    different_lines = set(file1_lines) ^ set(file2_lines)
    return common_lines, different_lines


def write_lines_to_file(lines, file_name):
    with open(file_name, 'w') as file:
        for line in lines:
            file.write(line)


def main():
    ...


if __name__ == "__main__":
    main()