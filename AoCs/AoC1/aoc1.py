def collectFromList():
    result_sum = 0
    path = '../Advent_of_Code/AoCs/AoC1/2023-01-1-input.txt'
    for line_lf in open(path):
        result = outer_digits(line_lf.rstrip())
        if result == '':
            continue
        else:
            result_sum += int(result)
    print(result_sum)
def outer_digits(inputString):
    x = ''
    y = ''
    for characters in inputString:
        if characters.isdigit():
            if(x == ''):
                x = characters
            else:
                y = characters
    if y == '':
        return x + x
    else:
        return x + y

if __name__ == '__main__':
    collectFromList()