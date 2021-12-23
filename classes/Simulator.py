from classes.Visualizer import Visualizer
from random import random

from classes.Plant import Plant
from classes.Herbivorous import Herbivorous
from classes.Carnivores import Carnivores

class Simulator:

  # TODO: Implement Dependency Injections
  visualizer: Visualizer
  p: tuple[float, float, float, float]
  g: tuple[float, float]
  carnivores_life_cycle: dict[tuple[int, int], tuple[bool, int | str]] = {}

  # Constructor
  def __init__(self, visualizer, p, g) -> None:
    self.visualizer = visualizer
    self.p = p
    self.g = g

    # Initializing calls
    self.init_board()
    self.init_cells()
    self.save_board()

  # Fill created board with values
  def fill(self) -> None:
    self.init_cells()

  # Update function call
  def step(self) -> None:
    if self.visualizer.current_i == self.visualizer.i:
      raise IndexError('Out of steps')

    # Calculating intervals of distribution
    probability_context = self.init_interval(self.g)

    # Planting here
    for i in range(len(self.visualizer.board)):
      for j in range(len(self.visualizer.board[i])):
        if self.visualizer.board[i][j] == self.visualizer.labels['empty'] or self.visualizer.board[i][j] == self.visualizer.labels['plant']:
          plant = Plant(i, j)
          self.visualizer.board = plant.life_cycle(self.visualizer.board, self.visualizer.labels, probability_context)

    # Spawning herbivorous
    for i in range(len(self.visualizer.board)):
      for j in range(len(self.visualizer.board[i])):
        if self.visualizer.board[i][j] == self.visualizer.labels['herbivorous']:
          herbivorous = Herbivorous(i, j)
          self.visualizer.board = herbivorous.life_cycle(self.visualizer.board, self.visualizer.labels)

    # Carnivorous update
    for i in range(len(self.visualizer.board)):
      for j in range(len(self.visualizer.board[i])):
        if self.visualizer.board[i][j] == self.visualizer.labels['carnivores']:
          stat = self.carnivores_life_cycle.get((i, j), (False, 0))
          carnivores = Carnivores(i, j, stat)
          self.visualizer.board = carnivores.life_cycle(
            self.visualizer.board,
            self.visualizer.labels
          )
          # clearing dead bodies - life is a bitch
          self.clear(carnivores)

    # Drawing frame, iteration
    self.visualizer.current_i += 1
    self.draw()

  # Updating carnovorous and killing them if they die, then clearing cell
  # so that the plant can grow etc.
  def clear(self, carnivores: Carnivores) -> None:
    if carnivores.was_moved and (carnivores.x_prev, carnivores.y_prev) in self.carnivores_life_cycle.keys():
      del self.carnivores_life_cycle[(carnivores.x_prev, carnivores.y_prev)]

    self.carnivores_life_cycle[(carnivores.x, carnivores.y)] = (carnivores.was_moved, carnivores.life_energy_left)

    # It lived enough
    if self.carnivores_life_cycle[(carnivores.x, carnivores.y)][1] == 5:
      del self.carnivores_life_cycle[(carnivores.x, carnivores.y)]
      self.visualizer.board[carnivores.x][carnivores.y] = self.visualizer.labels['empty']

  # Same old numpy.zeros, but with labels
  def init_board(self) -> None:
    self.visualizer.board = [
      [
        self.visualizer.labels['empty'] for _ in range(self.visualizer.h)
      ] for _ in range(self.visualizer.w)
    ]

  # Saving board in csv format, so that you can see it
  # TODO: Change to json
  def save_board(self, filename='board.csv') -> None:
    f = open(filename, 'w')
    f.write(str(self.visualizer))
    f.close()

  def init_cells(self) -> None:
    # take plant probability from probabilities
    plant_probability = self.p[-1]
    probabilities = self.p[:-1]

    # init plants on board
    self.visualizer.board = [
      [
        self.visualizer.labels['plant'] if random() < plant_probability else cell for cell in row
      ] for row in self.visualizer.board
    ]

    # Calculating intervals of distribution
    probability_context = self.init_interval(probabilities)

    # Adding labels instead of old numbers 0, 1, 2, 3
    for i in range(len(self.visualizer.board)):
      for j in range(len(self.visualizer.board[i])):
        if self.visualizer.board[i][j] == self.visualizer.labels['empty']:
          num = random()
          interval = self.find_probability_interval(probability_context, num)
          index = probability_context.index(interval)

          if index == 0:
            self.visualizer.board[i][j] = self.visualizer.labels['empty']
          elif index == 1:
            self.visualizer.board[i][j] = self.visualizer.labels['herbivorous']
          elif index == 2:
            self.visualizer.board[i][j] = self.visualizer.labels['carnivores']

  # Calculating interval of distribution
  # TODO: Make self-sufficient module for such math or use numpy
  def init_interval(self, probabilities: tuple[float, float, float]) -> tuple[tuple[float, float]]:
    return tuple(
      (
        float(sum(probabilities[:i])),
        float(sum(probabilities[:i]) + probabilities[i])
      ) for i in range(len(probabilities))
    )

  # TODO: ALSO Make self-sufficient module for such math or use numpy
  def find_probability_interval(self, probability_context: tuple[tuple[float, float]], num: float) -> tuple[float, float]:
    return next(interval for interval in probability_context if interval[0] <= num <= interval[1])

  # TODO: Beautify a little, because looks terrible
  def draw(self) -> None:
    # self.visualizer.clear()

    # TODO: Create side borders too
    border = 'x+' * 4 * (self.visualizer.w - 1) + 'x'

    # Printing gameboard to the console
    print(border)
    print(str(self.visualizer))
    print(border)
