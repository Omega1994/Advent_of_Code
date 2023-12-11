def collectFromList():
    result_sum = 0
    #path = '../Advent_of_Code/AoCs/AoC1/2023-01-1-input.txt'
    path = '../AoC-Input/2023-01-1-input.txt'
    for line_lf in open(path):
        line_strip = line_lf.rstrip()
        altered_val = digit_in_string(line_strip)
        result = outer_digits(altered_val)
        if result == '':
            continue
        else:
            result_sum += int(result)
    print(result_sum)

def digit_in_string(inputString):
    dictionary = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
                  'eight': '8', 'nine': '9'}
    found_digit_list =[]
    for digit in dictionary:
        if digit in inputString:
            first = inputString.find(digit)
            found_digit_list.append((first, digit))
            last = inputString.rfind(digit)
            if last != first:
                found_digit_list.append((last, digit))
    found_digit_list.sort()
    if len(found_digit_list) >= 2:
        last_replace = found_digit_list.pop(-1)
        inputString = call_replace(inputString, last_replace, dictionary)
        first_replace = found_digit_list.pop(0)
        inputString = call_replace(inputString, first_replace , dictionary)
        print(inputString)
    elif len(found_digit_list) == 1:
        inputString = call_replace(inputString, found_digit_list.pop(0), dictionary)
    return inputString

def call_replace(inputString, replace_tuple, dictonary):
    start = replace_tuple[0]
    end = start + len(replace_tuple[1]) - 1
    replace_val = dictonary.get(replace_tuple[1])
    return replacer_of_string_into_num(inputString, start, end, replace_val)



def replacer_of_string_into_num(inputString, start, ende, replacement_value):
    return f'{inputString[0:start]}{replacement_value}{inputString[ende:]}'

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