from math import isclose
from time import sleep

from classes.Visualizer import Visualizer
from classes.Simulator import Simulator


if __name__ == '__main__':
  w = int(input('Введите ширину поля: '))
  h = int(input('Введите высоту поля: '))

  p_3 = float(input('Введите вероятность появления растений в пустых клетках: '))

  if p_3 >= 1:
    raise ValueError('Вероятность не должна быть > 1')

  print("ВНИМАНИЕ: Следующие 3 вероятности должны в сумме быть равны 1")
  p_0 = float(input('Введите вероятность того, что клетка будет пустой: '))
  p_1 = float(input('Введите вероятность того, что в клетке будет травоядное: '))
  p_2 = float(input('Введите вероятность того, что в клетке окажется хищник: '))

  p = (p_0, p_1, p_2, p_3)

  if not isclose(sum(p[:-1]), 1.0):
    raise ValueError("Неверное распределение - сумма вероятностей не равна 1")

  i = int(input('Сколько циклов над игрой произвести: '))

  g_3 = float(input('Введите вероятность появления растения в пустой клетке: '))
  g_0 = 1 - g_3

  g = (g_0, g_3)

  if not (g_3 >= 0 and g_3 <= 1):
    raise ValueError('Вероятность должна быть между 0 и 1')

  visualizer = Visualizer(w, h, i)
  simulator = Simulator(visualizer, p, g)

  for _ in range(i):
    simulator.step()
