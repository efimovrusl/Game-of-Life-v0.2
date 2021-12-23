from classes.Plant import *

from random import seed
import unittest

class TestPlant(unittest.TestCase):
  def test_init(self) -> None:
    mocked_cordinated = (1, 2)
    
    plant = Plant(*mocked_cordinated)

    cordinated = (plant.x, plant.y,)

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

    probability_interval = (
      (0, 0.5),
      (0.5, 1.0),
    )

    plant = Plant(1, 0)

    seed(11)

    board = plant.life_cycle(board, labels, probability_interval)

    mocked_board = [
      [1, 0, 1],
      [0, 0, 0]
    ]

    self.assertListEqual(
      board,
      mocked_board
    )

  def test_find_probability_interval(self) -> None:
    plant = Plant(1, 2)

    probability_interval = (
      (0.0, 0.3),
      (0.3, 0.7),
      (0.7, 1.0),
    )

    intervel = plant.find_probability_interval(probability_interval, 0.65)

    mocked_intervel = (0.3, 0.7)
    
    self.assertEqual(intervel, mocked_intervel)
