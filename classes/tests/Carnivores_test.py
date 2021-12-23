from classes.Carnivores import *

from random import seed
import unittest

class TestHerbivorous(unittest.TestCase):
  def test_init(self) -> None:
    mocked_cordinated = (1, 2)
    mocked_stat = (False, 0)
    
    carnivores = Carnivores(*mocked_cordinated, mocked_stat)

    cordinated = (carnivores.x, carnivores.y,)

    self.assertEqual(cordinated, mocked_cordinated)

  def test_life_cycle(self) -> None:
    board = [
      [1, 0, 1],
      [3, 0, 2]
    ]

    labels = {
      'empty': 0,
      'herbivorous': 1,
      'carnivores': 2,
      'plant': 3,
    }

    carnivores = Carnivores(1, 2, (False, 0))

    seed(11)

    board = carnivores.life_cycle(board, labels)

    mocked_board = [
      [1, 0, 0],
      [3, 0, 2]
    ]

    self.assertListEqual(
      board,
      mocked_board
    )

  def test_eat(self) -> None:
    board = [
      [1, 0, 1],
      [3, 0, 2]
    ]

    labels = {
      'empty': 0,
      'herbivorous': 1,
      'carnivores': 2,
      'plant': 3,
    }

    carnivores = Carnivores(1, 2, (False, 0))

    seed(11)

    board = carnivores.life_cycle(board, labels)

    mocked_board = [
      [1, 0, 0],
      [3, 0, 2]
    ]

    self.assertListEqual(
      board,
      mocked_board
    )

  def test_move(self) -> None:
    board = [
      [1, 0, 0],
      [3, 0, 2]
    ]

    labels = {
      'empty': 0,
      'herbivorous': 1,
      'carnivores': 2,
      'plant': 3,
    }

    carnivores = Carnivores(1, 2, (False, 0))

    seed(11)

    board = carnivores.life_cycle(board, labels)

    mocked_board = [
      [1, 0, 0],
      [3, 2, 0]
    ]

    self.assertListEqual(
      board,
      mocked_board
    )
