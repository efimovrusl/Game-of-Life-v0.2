from classes.Simulator import *
from classes.Visualizer import *
from helpers import *
from init import *
from old_main import *

from random import seed
import unittest

class TestCompering(unittest.TestCase):
  def test_compering(self) -> None:
    w = h = 5
    p = (0.5, 0.3, 0.4, 0.5)
    g = (0.5, 0.5)
    i = 1

    seed(10)

    board_func = init_board(w, h)
    board_func = init_cells(board_func, p)
    
    for _ in range(i):
      board_func = iter_board(board_func, g)

    save_board(board_func, 'board_fun.csv')

    seed(10)

    visualizer = Visualizer(w, h, i)
    simulator = Simulator(visualizer, p, g)

    for _ in range(i):
      simulator.step()

    board_class = simulator.visualizer.board

    save_board(board_class, 'board_class.csv')

    b1 = read_board('board_fun.csv')
    b2 = read_board('board_class.csv')

    self.assertListEqual(
      b1,
      b2
    )
