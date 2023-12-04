def games_possible():
    dict_stone_accessable = {'red': 12, 'green': 13, 'blue': 14}
    games = read_game_file()
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
    path = '../Advent_of_Code/AoCs/AoC2/2023-02-1-input.txt'
    listed_games = []
    for lines in open(path):
        lines = lines.rstrip('\n')
        if len(lines) > 0:
            listed_games.append(lines.rstrip('\n'))
    return listed_games

if __name__ == '__main__':
    print(games_possible())