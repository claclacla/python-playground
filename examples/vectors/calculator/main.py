from vectors_operations.operations.add import add as vectors_add
from vectors_operations.operations.subtract import subtract as vectors_subtract

from operations.multiply import *

def main():
  vector_a = [1, 2]
  vector_b = [4, 1]
  
  # Vectors addition

  print("Vectors addition:")

  try:
    vector_c = vectors_add([vector_a, vector_b])
  except Exception as exception:
    print(exception)
    return

  print(vector_c)

  # Vectors subtraction

  print("Vectors subtraction:")

  try:
    vector_d = vectors_subtract([vector_a, vector_b])
  except Exception as exception:
    print(exception)
    return

  print(vector_d)

  # Multiplication

  print("Multiplication:")

  vector_e = multiply(vector_a, 2)

  print(vector_e)

if __name__ == "__main__":
  main()