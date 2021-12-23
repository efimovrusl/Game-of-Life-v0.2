from helpers import display_board, init_interval, find_probability_interval
from random import random


# Task 1
def init_board(width: int, height: int) -> list[list[int]]:
    return [[0 for _ in range(width)] for _ in range(height)]


# Task 2
def init_cells(board: list[list[int]], probabilities: tuple[float]) -> list[list[int]]:
    # take plant probability from probabilities
    plant_probability = probabilities[-1]
    probabilities = probabilities[:-1]

    # Planting some plants
    board = [[3 if random() < plant_probability else cell for cell in row] for row in board]

    # Initialing intervals of distribution
    probability_context = init_interval(probabilities)

    # Spawning animals
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:

                # TODO: Change to LCG random generator
                num = random()
                interval = find_probability_interval(probability_context, num)

                # Filling board with probabilities
                board[i][j] = probability_context.index(interval)

    return board


def init_main() -> list[list[int]]:
    
    # Size input
    width = int(input('Input width of gaming board: '))
    height = int(input('Input height of gaming board: '))

    board = init_board(width, height)

    # Draw initialized board
    display_board(board)

    return board


# Task 1
if __name__ == '__main__':
    init_main()
