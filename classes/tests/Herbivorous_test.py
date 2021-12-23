from classes.Herbivorous import *

from random import seed
import unittest

class TestHerbivorous(unittest.TestCase):
  def test_init(self) -> None:
    mocked_cordinated = (1, 2)
    
    herbivorous = Herbivorous(*mocked_cordinated)

    cordinated = (herbivorous.x, herbivorous.y,)

    self.assertEqual(cordinated, mocked_cordinated)

  def test_life_cycle(self) -> None:
    board = [
      [1, 0, 1],
      [3, 0, 0]
    ]

    labels = {
      'empty': 0,
      'herbivorous': 1,
      'carnivores': 2,
      'plant': 3,
    }

    herbivorous = Herbivorous(0, 0)

    seed(11)

    board = herbivorous.life_cycle(board, labels)

    mocked_board = [
      [1, 0, 1],
      [3, 0, 0]
    ]

    self.assertListEqual(
      board,
      mocked_board
    )

  def test_eat(self) -> None:
    board = [
      [1, 0, 1],
      [3, 0, 0]
    ]

    labels = {
      'empty': 0,
      'herbivorous': 1,
      'carnivores': 2,
      'plant': 3,
    }

    herbivorous = Herbivorous(0, 0)

    seed(11)

    board = herbivorous.eat(board, labels)

    mocked_board = [
      [1, 0, 1],
      [3, 0, 0]
    ]

    self.assertListEqual(
      board,
      mocked_board
    )
