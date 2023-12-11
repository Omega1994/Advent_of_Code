def lottery_game():
    games = read_file()
    won_values = []
    for game in games:
        won_val = compare_winning_numbers(game[0], game[1])
        won_values.append(won_val)
    return sum(won_values)


def compare_winning_numbers(winning, your):
    won = 0
    for number in winning:
        if number in your:
            if won == 0:
                won += 1
            else:
                won = won * 2
    return won

def lottery_game_appending():
    games = read_file()
    prefix = 'Game '
    lookup_games = create_lookup_games(games, prefix)
    for index, game in enumerate(games):
        numbers_in_common = compare_with_winning(game[0], game[1])
        lookup_games = update_lookup(lookup_games, prefix, index, numbers_in_common)

    sum = 0
    for lookup in lookup_games:
        sum += lookup_games.get(lookup)

    return sum

def create_lookup_games(games, prefix):
    lookup = {}
    for index, game in enumerate(games):
        lookup.update({(prefix + str(index)): 1})
    return lookup

def compare_with_winning(winning, your):
    won = 0
    for number in winning:
        if number in your:
            won += 1
    return won

def update_lookup(lookup, prefix, index, numbers_in_common):
    label_current_entry = prefix + str(index)
    quantity = lookup.get(label_current_entry)
    for i in range(1, numbers_in_common + 1):
        label_updated_entry = prefix + str(index + i)
        if lookup.__contains__(label_updated_entry):
            amount = lookup.get(label_updated_entry) + quantity
            lookup.update({label_updated_entry: amount})
        else:
            break
    return lookup

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
    print(lottery_game_appending())