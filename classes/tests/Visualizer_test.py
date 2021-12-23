from classes.Visualizer import *

import unittest

class TestPlant(unittest.TestCase):
  def test_init(self) -> None:
    mocked_params = (2, 3, 3)
    
    visualizer = Visualizer(*mocked_params)

    params = (visualizer.w, visualizer.h, visualizer.i)

    self.assertEqual(params, mocked_params)

  def test_set_entities(self) -> None:
    visualizer = Visualizer(2, 3, 3)
    entities = [
      'empty',
      'herbivorous',
      'carnivores',
      'plant',
    ]

    visualizer.set_entities(entities)

    mocked_entities = [
      'carnivores',
      'empty',
      'herbivorous',
      'plant'
    ]

    self.assertListEqual(
      visualizer.entities,
      mocked_entities
    )

  def test_clear(self) -> None:
    visualizer = Visualizer(2, 3, 3)

    visualizer.clear()
    
    self.assertLogs(None)

  def test_serialize(self) -> None:
    visualizer = Visualizer(2, 3, 3)

    visualizer.board = [
      [1, 0, 1],
      [3, 0, 0]
    ]

    serialized = str(visualizer)
    mocked_serialize = '1\t0\t1\n3\t0\t0'
    
    self.assertEqual(serialized, mocked_serialize)
