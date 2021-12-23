from random import random

class Plant:

  # Coordinates in world (game board)
  x: int
  y: int

  # Constructor
  def __init__(self, x, y) -> None:
    self.x = x
    self.y = y

  # Update function
  def life_cycle(self, board: list[list[int]], labels, probability_context) -> list[list[int]]:
    
    # random to check whether it shall die or not
    num = random()
    interval = self.find_probability_interval(probability_context, num)
    index = probability_context.index(interval)

    # Dying or living for another cycle
    board[self.x][self.y] = labels['empty'] if index == 0 else labels['plant']  # 0 index for 0 and any other index for 3
    
    # Updating board
    return board

  # TODO: Move to outer class
  def find_probability_interval(self, probability_context: tuple[tuple[float, float]], num: float) -> tuple[float, float]:
    return next(interval for interval in probability_context if interval[0] <= num <= interval[1])
