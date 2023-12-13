def racing():
    time, distance = reading_file()
    race_optimizer = []
    for i in range(len(time)):
        margine = check_race(time[i], distance[i])
        race_optimizer.append(margine)
    return mult_list_val(race_optimizer)

def check_race(time, length):
    range_of_margin = 0
    for i in range(1, time - 1):
        distance = i * (time - i)
        if distance > length:
            range_of_margin += 1
    return range_of_margin

def mult_list_val(race_val):
    mult = 1
    for i in race_val:
        mult *= i
    return mult
def reading_file():
    path = ('../AoC-Input/aoc-6-test-input.txt')
    time = []
    distance = []
    for line in open(path):
        line = line.rstrip("\n")
        if line.startswith("Time:"):
            time = extract_num(time, line)
        elif line.startswith("Distance:"):
            distance = extract_num(distance, line)
    return (time, distance)

def extract_num(list_instance, line):
    accumulator = ""
    for i in line:
        if i.isdigit():
            accumulator += i
        else:
            if accumulator != "":
                list_instance.append(int(accumulator))
                accumulator = ""
    if (accumulator != ""):
        list_instance.append(int(accumulator))
    return list_instance

def racing_part_two():
    time, distance = read_file()
    amount = check_race(time, distance)
    return amount

def read_file():
    path = ('../AoC-Input/aoc-6-input.txt')
    time = 0
    distance = 0

    for line in open(path):
        line = line.rstrip("\n")
        if line.startswith("Time:"):
            time = read_number(line)
        elif line.startswith("Distance:"):
            distance = read_number(line)
    return time, distance

def read_number(line):
    number = ""
    for c in line:
        if c.isdigit():
            number += c
    return int(number)

if __name__ == '__main__':
    print(racing_part_two())