def lottery_game():
    games = read_file()
    won_values = []
    for game in games:
        won_val = compare_winning_numbers(game[0], game[1])
        won_values.append(won_val)
    return sum(won_values)

def read_file():
    path = '../AoC-Input/aoc-4-input.txt'
    games = []
    for line in open(path):
        line = line.rstrip("\n")
        splitting_prefix = line.split(":")
        splitting_winning_numbers = splitting_prefix[1].split("|")
        winning = reading_numbers(splitting_winning_numbers[0])
        your_numbers = reading_numbers(splitting_winning_numbers[1])
        games.append([winning, your_numbers])
    return games

def compare_winning_numbers(winning, your):
    won = 0
    for number in winning:
        if number in your:
            if won == 0:
                won += 1
            else:
                won = won * 2
    return won

def reading_numbers(input_val):
    number = []
    num = ''
    for c in input_val:
        if c.isdigit():
            num += c
        else:
            if num != '':
                number.append(int(num))
                num = ''
    if num != '':
        number.append(int(num))
    return number

if __name__ == '__main__':
    print(lottery_game())