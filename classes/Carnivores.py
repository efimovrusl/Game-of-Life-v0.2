from random import randrange, choice


class Carnivores():

  # Attributes - coordinates and states
  x: int
  y: int
  x_prev: int
  y_prev: int
  r_eat: int = 1
  r_move: int = 3
  was_eaten: bool = False
  was_moved: bool = False
  life_energy_left: int = 0

  # Constructor
  def __init__(self, x, y, stat) -> None:
    self.x = x
    self.y = y
    self.x_prev = x
    self.y_prev = y
    self.was_moved = stat[0]
    self.life_energy_left = stat[1]

  # Update function
  def life_cycle(self, board: list[list[int]], labels) -> list[list[int]]:
    if self.was_moved:
      return board
      
    self.was_eaten = False

    board = self.eat(board, labels)

    # Energy calculation
    if not self.was_eaten:
      board = self.move(board, labels)
      self.life_energy_left += 1
    else:
      self.life_energy_left = 0

    return board

  # Check if animal can eat and do so if possible
  def eat(self, board: list[list[int]], labels) -> list[list[int]]:
    hunt_top_cut = 0 if self.x - self.r_eat < 0 else self.x - self.r_eat
    hunt_bottom_cut = len(board) if self.x + self.r_eat + 1 >= len(board) else self.x + self.r_eat + 1
    hunt_left_cut = 0 if self.y - self.r_eat < 0 else self.y - self.r_eat
    hunt_right_cut = len(board[self.x]) if self.y + self.r_eat >= len(board[self.x]) else self.y + self.r_eat

    # Temp variables
    herbivorous_count, carnivores_count = 0, 0

    # Counting animals around to check if you can eat someone
    # And later do so
    for k in range(hunt_top_cut, hunt_bottom_cut):
      for e in range(hunt_left_cut, hunt_right_cut):
        if (self.x, self.y) != (k, e):
          if board[k][e] == labels['herbivorous']:
            herbivorous_count += 1
          elif board[k][e] == labels['carnivores']:
            carnivores_count += 1

    # Literally eating
    if herbivorous_count >= 1:
      herbivorous_to_eat = 1
      self.was_eaten = True

      # OH WE HAVE FOOD AND PARTNER, LET'S HAVE SOME S*X!!!
      if carnivores_count >= 1 and herbivorous_count >= 2:
        herbivorous_to_eat = 2

      # Defining random direction for spawning child
      row_index = randrange(hunt_top_cut, hunt_bottom_cut)
      cell_index = randrange(hunt_left_cut, hunt_right_cut)

      # Killing herbivorous, which were eaten
      while herbivorous_to_eat:
        if board[row_index][cell_index] == labels['herbivorous'] and herbivorous_to_eat:
          board[row_index][cell_index] = labels['carnivores'] if herbivorous_to_eat == 2 else labels['empty']
          herbivorous_to_eat -= 1

        # Defining random direction again
        row_index = randrange(hunt_top_cut, hunt_bottom_cut)
        cell_index = randrange(hunt_left_cut, hunt_right_cut)

    # Updating the board
    return board

  # We can move and se obstacles, but also food to eat, so let's move
  def move(self, board: list[list[int]], labels) -> list[list[int]]:

    # Limiting by top border
    if self.x - self.r_move < 0:
      move_top_cut = 0
    else:
      move_top_cut = self.x - self.r_move

    # Limiting by bottom border
    if self.x + self.r_move + 1 >= len(board):
      move_bottom_cut = len(board)
    else:
      move_bottom_cut = self.x + self.r_move + 1

    # Limiting by left border
    if self.y - self.r_move < 0:
      move_left_cut = 0
    else:
      move_left_cut = self.y - self.r_move

    # Limiting by right border
    if self.y + self.r_move + 1 >= len(board[self.x]):
      move_right_cut = len(board[self.x])
    else:
      move_right_cut = self.y + self.r_move + 1

    # Food, which we wanna eat and can see
    herbivorous = []

    # Counting herbovorous, which we wanna eat and see around
    for k in range(move_top_cut, move_bottom_cut):
      for e in range(move_left_cut, move_right_cut):
        if (self.x, self.y) != (k, e):
          if board[k][e] == labels['herbivorous']:
            herbivorous.append((k, e))

    # Kinda pathfinder to move towards seen herbivorous
    if len(herbivorous):
      distances = {herb: (((herb[1] - self.y) ** 2) + ((herb[0] - self.x) ** 2)) ** 0.5 for herb in herbivorous}
    
      # Sorting paths
      ordered_distances = dict(sorted(distances.items(), key=lambda item: item[1]))

      for closest in ordered_distances:
        # Closest from top
        if closest[0] - 1 < move_top_cut:
          close_top_cut = move_top_cut
        else:
          close_top_cut = closest[0] - 1

        # Closest from bottom
        if closest[0] + 2 >= move_bottom_cut:
          close_bottom_cut = move_bottom_cut
        else:
          close_bottom_cut = closest[0] + 2

        # Closest from left
        if closest[1] - 1 < move_left_cut:
          close_left_cut = move_left_cut
        else:
          close_left_cut = closest[1] - 1

        # Closest from right
        if closest[1] + 2 >= move_right_cut:
          close_right_cut = move_right_cut
        else: 
          close_right_cut = closest[1] + 2

        # List of cells, where you can move
        empty_cells = []

        # Selecting empty cells
        for k in range(close_top_cut, close_bottom_cut):
          for e in range(close_left_cut, close_right_cut):
            if closest != (k, e):
              if board[k][e] == labels['empty']:
                empty_cells.append((k, e))

        # Trying to move towards closest food (herbivorous)
        if len(empty_cells):
          row_index, cell_index = choice(empty_cells)
          board[row_index][cell_index] = labels['carnivores']
          board[self.x][self.y] = labels['empty']
          self.x_prev = self.x
          self.y_prev = self.y
          self.x = row_index
          self.y = cell_index
          self.was_moved = True

          break
    # Updating board
    return board
