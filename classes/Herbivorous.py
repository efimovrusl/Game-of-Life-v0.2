from random import randrange

class Herbivorous:
  
  # Coordinates and states
  x: int
  y: int
  r_eat: int = 2
  was_eaten: bool = False

  # Constructor
  def __init__(self, x, y) -> None:
    self.x = x
    self.y = y

  # Update function
  def life_cycle(self, board: list[list[int]], labels) -> list[list[int]]:
    self.was_eaten = False

    board = self.eat(board, labels)

    return board

  # Check if animal can eat and do so if possible
  def eat(self, board: list[list[int]], labels) -> list[list[int]]:
    
    # Limiting by top border
    if self.x - self.r_eat < 0:
      top_cut = 0
    else:
      top_cut = self.x - self.r_eat

    # Limiting by bottom border
    if self.x + self.r_eat + 1 >= len(board):
      bottom_cut = len(board)
    else:
      bottom_cut = self.x + self.r_eat + 1

    # Limiting by left border
    if self.y - self.r_eat < 0:
      left_cut = 0
    else:
      left_cut = self.y - self.r_eat

    # Limiting by right border
    if self.y + self.r_eat + 1 >= len(board[self.x]):
      right_cut = len(board[self.x])
    else:
      right_cut = self.y + self.r_eat + 1

    plant_count, herbivorous_count = 0, 0

    # Counting plants and same-typed animals around
    for k in range(top_cut, bottom_cut):

      for e in range(left_cut, right_cut):

        if (self.x, self.y) != (k, e):
          if board[k][e] == labels['plant']:
            plant_count += 1
          elif board[k][e] == labels['herbivorous']:
            herbivorous_count += 1

    # Condition for breeding
    if herbivorous_count >= 1 and plant_count >= 4:
      plant_count, herbivorous_count = 4, 1

      row_index = randrange(top_cut, bottom_cut)

      cell_index = randrange(left_cut, right_cut)

      while plant_count or herbivorous_count:

        if board[row_index][cell_index] == labels['plant'] and plant_count:
          board[row_index][cell_index] = labels['empty']
          plant_count -= 1

        elif board[row_index][cell_index] == labels['herbivorous'] and herbivorous_count:
          board[row_index][cell_index] = labels['herbivorous']
          herbivorous_count -= 1

        # Choosing cell around to place a child
        row_index = randrange(top_cut, bottom_cut)
        cell_index = randrange(left_cut, right_cut)
    
    return board
  