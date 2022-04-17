import time


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1. Creando un iterador
my_iter = iter(my_list)

# Esta es la manera interna en como funciona un ciclo for. El for ... in es sugar sintax para recorrer un iterador.
while True:
    try:
        # 2. Iterando un iterador, Consecutivamente hasta que termine
        element = next(my_iter)
        print(element)
        # 3. Cuando no queden datos en el iterador, la excepción StopIteration es elevada
    except StopIteration:
        print("--------------------------------")
        break


class EvenNumbers:
  """
    Clase que implementa un iterador de todos los números pares, o los números pares hasta un máximo
  """

  # Constructor de la clase
  # self hace referencia al objeto futuro que voy a crear con esta clase
  def __init__(self, max = None):
    self.max = max

  # Método para tener elementos o atributos que voy a necesitar para que el iterador funcione
  def __iter__(self):
    self.num = 0 # Primer número par
    return self

  # Método para tener la función "next" de Python
  def __next__(self):
    if not self.max or self.num <= self.max:
      result = self.num
      self.num += 2
      return result
    else:
      raise StopIteration


class FiboIter():
    def __init__(self):
        pass

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            # self.n1 = self.n2
            # self.n2 = self.aux
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            return self.aux

if __name__ == '__main__':
    even_numbers = EvenNumbers(10)
    for element in even_numbers:
        print(element)
    print("------------------------------------------------")

    fibonacci = FiboIter()
    for element in fibonacci:
        print(element)
        time.sleep(0.5)
