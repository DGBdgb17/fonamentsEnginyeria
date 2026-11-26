# llibreria per generar numeros aleatoris
import random

# llibreria per mostrar gràfiques
import matplotlib.pyplot as plt




PI = 3.1416









def generar_valor_aleatori(maxim: int, offset: int=0) -> float:
  """
  Aquesta funció retorna un valor aleatori dins un rang donada la seva longitud i un offset respecte el 0.
  Per exemple, si volem números entre l'1 i el 3, podem definir com a arguments maxim=2 i offset=1

  Args:
    maxim: el nombre de valors que volem
    offset: la separació del valor inicial respecte el 0

  Returns:
  Un valor aleatori dins el rang definit
  """
  return random.random() * maxim + offset




def area_cercle_monte_carlo(radi: float, punts_maxims: int) -> tuple[float, tuple[list, list], tuple[list, list]]:
  """
  Aquesta funcio calcula l'area d'un cercle a partir d'un radi
  utilitzant el mètode de Monte Carlo. Inscriu el cercle dins un cuadrat de
  costat radi x 2 i llença N punts aleatoris.

  Args:
    radi: radi del cercle
    punts_maxims: punts a generar dins el cuadrat on està inscrit el cercle

  Returns: una tupla on el primer valor es l'aproximació de l'àrea, el segon valor es
  una tupla amb els punts dins el cercle i el tercer valor una tupla amb els punts fora del cercle.
  Aquestes tuples de punts tenen la forma ([x1, ..., xn], [y1, ..., yn]) per adaptarse millor
  a com demana dades la llibreria matplotlib
  """
  punts_dins = ([], [])
  punts_fora = ([], [])

  dentro = 0

  for _ in range(punts_maxims):
    punto = (generar_valor_aleatori(radi*2, -radi), generar_valor_aleatori(radi*2, -radi))

    if (punto[0]**2 + punto[1]**2) <= radi**2: # Si el punt està dins el cercle
      punts_dins[0].append(punto[0])
      punts_dins[1].append(punto[1])
      dentro += 1
    else:
      punts_fora[0].append(punto[0])
      punts_fora[1].append(punto[1])

  # Calcul de l'àrea respecte l'àrea del cuadrat on el cercle està inscrit
  area_monte_carlo = (dentro/punts_maxims) * (2*radi)**2

  return area_monte_carlo, punts_dins, punts_fora




def demanar_dades() -> float:
  """
  Aquesta funció demana el valor del radi a l'usuari i retorna el seu valor
  com a valor decimal. En cas que l'usuari no entri un valor correcte el torna a demanar.

  Returns:
  El valor entrat per l'usuari
  """

  while True:
    try:
      return float(input("Entra el valor del radi: "))
    except:
      print("ERROR: entra un número decimal")




def _exemple_punt_dins_cercle():
  """
  Procediment d'ajuda per la presentació, mostra com s'utilitza pitàgores
  per calcular si un punt està dins o no del cercle.
  """

  plt.gca().add_artist(plt.Circle((0,0), 1, color="#FFFF99"))
  plt.plot([0,0.8,0.8,0], [0,0,0.8,0], "o-", color="r")
  plt.plot([0,-0.3,-0.3,0], [0,0,0.3,0], "o-",color="g")
  plt.axis("scaled")
  plt.show()


def main():
  """
  Programa principal
  """

  radi = demanar_dades()

  area_real = PI*radi**2

  for tests in [1000, 10000, 100000, 1000000]:
    area, punts_dins, punts_fora = area_cercle_monte_carlo(radi, tests)
    print("--- Per a", tests, "punts:")
    print("Area real:", area_real)
    print("Aproximació de l'àrea:", area)
    print("Aproximació de PI:", area/(radi**2)) # Aproximem PI aillant-lo de la fòrmula de l'area d'un cercle
    print()


    plt.gca().add_artist(plt.Circle((0,0), radi, color="#FFFF99"))
    plt.plot(punts_dins[0], punts_dins[1], ".", color="#DD3333")
    plt.plot(punts_fora[0], punts_fora[1], ".", color="#33DDDD")
    plt.axis('scaled')
    plt.show()







main()
# _exemple_punt_dins_cercle()

"""
Referencies consultades:

Ús de matplotlib per mostrar punts:
https://www.w3schools.com/python/matplotlib_plotting.asp
https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

Veure els punts preservant l'escala de l'espai on es troben
https://stackoverflow.com/questions/2934878/matplotlib-pyplot-preserve-aspect-ratio-of-the-plot

Dibuixar un cercle a matplotlib:
https://www.statology.org/matplotlib-circle/
"""