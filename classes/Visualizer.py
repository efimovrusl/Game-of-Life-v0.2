from os import system

class Visualizer:
  # Key characteristics
  w: int
  h: int
  i: int
  
  # iteration
  current_i: int = 0
  
  # data
  board: list[list[int]] = []
  
  # enum
  entities: list[str] = [
    'empty',
    'herbivorous',
    'carnivores',
    'plant',
  ]

  # костыль :)
  labels = {
    'empty': 0,
    'herbivorous': 1,
    'carnivores': 2,
    'plant': 3,
  }

  # Draw or NOT
  visual = True

  # Constructor
  def __init__(self, w, h, i) -> None:
    self.w = w
    self.h = h
    self.i = i

  # Loading entities to the gameboard
  def set_entities(self, entities: list[str]) -> None:
    copy: list[str] = entities[:]
    copy.append('empty')
    copy = list(set(copy))
    copy.sort()
    self.entities = copy

  # Clearing everything we can clean
  def clear(self) -> None:
    system('clear')

  # ToString()
  def __str__(self) -> str:
    return '\n'.join([ '\t'.join([ str(cell) for cell in row ]) for row in self.board ])
