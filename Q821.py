def print_bitmap(bitmap):
    if len(bitmap) <= 50:
        print(bitmap)
    else:
        print(bitmap[0:50])
        print_bitmap(bitmap[50:])

def division(a, b):
    if ((a + b) % 2 == 0):
        return int((a + b + 1) / 2)
    else:
        return int((a + b) / 2)

def check_bitmap_equality(matrix, begin_line, end_line, begin_column, end_column):
    item = matrix[begin_line][begin_column]
    for i in range(begin_line, end_line + 1):
        for j in range(begin_column, end_column + 1):
            if matrix[i][j] != item:
                return "-1"
    return str(item)

def bitmap(matrix, begin_line, end_line, begin_column, end_column):
    check = check_bitmap_equality(matrix, begin_line, end_line, begin_column, end_column)
    if(check != "-1"):
        return check
    else:
        if (begin_line >= end_line):
            middle_column = division(begin_column, end_column)
            return "D" + bitmap(matrix, begin_line, end_line, begin_column, middle_column) + bitmap(matrix, begin_line, end_line, middle_column + 1, end_column)
        elif (begin_column >= end_column):
            middle_line = division(begin_line, end_line)
            return "D" + bitmap(matrix, begin_line, middle_line, begin_column, end_column) + bitmap(matrix, middle_line + 1, end_line, begin_column, end_column)
        else:
            middle_line = division(begin_line, end_line)
            middle_column = division(begin_column, end_column)
            return "D" + bitmap(matrix, begin_line, middle_line, begin_column, middle_column) + bitmap(matrix, begin_line, middle_line, middle_column + 1, end_column) + bitmap(matrix, middle_line + 1, end_line, begin_column, middle_column) + bitmap(matrix, middle_line + 1, end_line, middle_column + 1, end_column)

cases = int(input())
for i in range(cases):
    data = input().split()
    lines = int(data[0])
    columns = int(data[1])
    matrix = []
    for j in range(lines):
        line = input()
        matrix.append([int(line[k]) for k in range(columns)])
    bm = str(bitmap(matrix, 0, lines - 1, 0, columns - 1))
    print_bitmap(bm)
