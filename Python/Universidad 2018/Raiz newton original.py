## Raíz cuadrada método de Newton-Raphson
## Versión 0
def raizNR0 (num, error):
  ## aproximar un número intermedio
  def aproximar_mejor (apr):
    return (apr + (num / apr)) / 2.0

  ## determinar si raíz es una buena aproximación
  def es_aceptable (aproximación):
    return abs (num - (aproximación * aproximación)) < error

  ## iniciar
  aprox = num / 2.0
  print ("aprox", aprox)

  ## buscar raíz por tangente (Newton-Raphson)
  while not (es_aceptable (aprox)):
    aprox = aproximar_mejor (aprox)
    print ("aprox", aprox)
  ## la raíz
  return aprox
