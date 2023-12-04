import os
import subprocess

#User gets a request to enter a number to open the directory
def open_aoc_directory(exercise):
    path_to_exercise_directory = '../Advent_of_Code/AoCs/AoC' + exercise

    if os.path.exists(path_to_exercise_directory):
        path_to_executed_file = 'aoc' + exercise + '.py'
        return os.path.join(path_to_exercise_directory, path_to_executed_file)
    else:
        print(f'Error: You Fucked Up! The requested Directory does not Exist!')

def execute_aoc(path, excercise):
    try:
        print(f'The Advent of Code Excercise {exercise} will be executed.')
        # capture_output let this process access the output data.
        return subprocess.run(['python', path], capture_output=True)

    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to execute . {e}")

if __name__ == '__main__':
    exercise = input('What Advent of Code do you want to execute: \n')
    path = open_aoc_directory(exercise)
    process_result = execute_aoc(path, exercise)
    #The process result is a byte value that needs to be decoded before using it in the current code
    print(f'The result of Advent of Code {exercise} is:\n{process_result.stdout.decode()}')