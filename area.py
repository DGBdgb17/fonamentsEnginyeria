# llibreria per generar numeros aleatoris
import random
import matplotlib.pyplot as plt

def aproximacio_monte_carlo(radi, punts_maxims, DECIMALS=1000):
  punts = []

  max_punto = radi*DECIMALS
  min_punto = -1*max_punto

  dentro = 0

  for i in range(punts_maxims):
    punto = ((random.randint(min_punto, max_punto))/DECIMALS,(random.randint(min_punto, max_punto))/DECIMALS)

    if (punto[0]**2 + punto[1]**2) < radi:
      dentro += 1
      punts.append((punto, True))
    else:
      punts.append((punto, False))

  area_monte_carlo = (dentro/punts_maxims) * (2*radi)**2

  return area_monte_carlo, punts


radi = int(input("Entra el valor del radi (numero entero): "))

PI = 3.1416

area_real = PI*radi**2

# print("Area real:", area_real)

for tests in [1000, 10000, 100000, 1000000]:
  area, punts = aproximacio_monte_carlo(radi, 1000)
  print("--- Per a", tests, "punts:")
  print("Area real:", area_real)
  print("Aproximació:", area)
  print()
  plt.scatter([x[0][0] for x in punts if x[1]], [ x[0][1] for x in punts if x[1]], color="r")
  plt.scatter([x[0][0] for x in punts if not x[1]], [ x[0][1] for x in punts if not x[1]], color="b")
  plt.show()

