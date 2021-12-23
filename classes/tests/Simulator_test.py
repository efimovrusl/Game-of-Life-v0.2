from classes.Simulator import Simulator
from classes.Visualizer import Visualizer

from pathlib import Path
from random import seed
import unittest

class TestPlant(unittest.TestCase):
  def assertIsFile(self, path):
    if not Path(path).resolve().is_file():
      raise AssertionError("File does not exist: %s" % str(path))

  def test_init(self) -> None:
    visualizer = Visualizer(2, 3, 3)
    p = (0.5, 0.3, 0.4, 0.3)
    g = (0.5, 0.5)

    mocked_params = (visualizer, p, g)

    simulator = Simulator(*mocked_params)

    params = (
      simulator.visualizer,
      simulator.p,
      simulator.g
    )

    self.assertEqual(params, mocked_params)

  def test_init_board(self) -> None:
    simulator = Simulator(
      Visualizer(2, 3, 3),
      (0.5, 0.3, 0.4, 0.3),
      (0.5, 0.5)
    )

    simulator.init_board()

    board = simulator.visualizer.board

    mocked_board = [
      [0, 0, 0],
      [0, 0, 0]
    ]

    self.assertListEqual(
      board,
      mocked_board
    )

  def test_save_board(self) -> None:
    simulator = Simulator(
      Visualizer(2, 3, 3),
      (0.5, 0.3, 0.4, 0.3),
      (0.5, 0.5)
    )

    simulator.visualizer.board = [
      [0, 0, 0],
      [0, 0, 0]
    ]

    simulator.save_board()

    self.assertIsFile('board.csv')

  def test_init_cells(self) -> None:
    simulator = Simulator(
      Visualizer(2, 3, 3),
      (0.5, 0.3, 0.4, 0.3),
      (0.5, 0.5)
    )

    simulator.visualizer.board = [
      [0, 0, 0],
      [0, 0, 0]
    ]

    seed(10)

    simulator.init_cells()

    board = simulator.visualizer.board

    mocked_board = [
      [1, 0, 1],
      [3, 0, 0]
    ]

    self.assertListEqual(
      board,
      mocked_board
    )
