def stone_game(fixed=False):
    games = read_game_file()
    if fixed:
        dict_stone_accessable = {'red': 12, 'green': 13, 'blue': 14}
        game_possible(dict_stone_accessable, games)
    else:
        game_dynamic_stone(games)

def game_dynamic_stone(games):
    sum_of_pow = 0
    for game in games:
        dict_stone = {'red': 0, 'green': 0, 'blue': 0}
        game = game.split(":")
        instances = game[1].split(";")
        for instance in instances:
            colour = instance.split(",")
            for col in colour:
                col = col[1:]
                splitted = col.split(" ")
                amount = int(splitted[0])
                color = splitted[1]
                if dict_stone.get(color) < amount:
                    update_color_amount = {color: amount}
                    dict_stone.update(update_color_amount)
        sum_of_pow = sum_of_pow + (dict_stone.get('red') * dict_stone.get('green') * dict_stone.get('blue'))
    return sum_of_pow


def game_possible(dict_stone_accessable, games):
    sum_possible_games = 0
    for game in games:
        game = modify_game_instance(game)
        game = game.split(":")
        game_id = int(game[0])
        instances = game[1].split(";")
        result = check_instances(instances, dict_stone_accessable)
        if result == True:
            sum_possible_games += game_id
    return sum_possible_games


def modify_game_instance(game):
    game = game.replace('Game ', '')
    return game

def check_instances(instances, dict_stone_accessable):
    for instance in instances:
        colour = instance.split(",")
        for col in colour:
            col = col[1:]
            splitted = col.split(" ")
            amount = int(splitted[0])
            color = splitted[1]
            if amount > dict_stone_accessable.get(color):
                return False
    return True

def read_game_file():
    #path = '../Advent_of_Code/AoCs/AoC2/2023-02-1-input.txt'
    path = '../AoC-Input/2023-02-1-input.txt'
    listed_games = []
    for lines in open(path):
        lines = lines.rstrip('\n')
        if len(lines) > 0:
            listed_games.append(lines.rstrip('\n'))
    return listed_games

if __name__ == '__main__':
    stone_game()