from vectors_operations.operations.add import add as vectors_add
from vectors_operations.operations.subtract import subtract as vectors_subtract

from operations.multiply import *
from operations.magnitude import *
from operations.direction import *

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

  # Magnitude

  print("Magnitude:")

  vector_magnitude = magnitude([-0.221, 7.437])

  print(vector_magnitude)

  # Direction

  print("Direction:")

  vector_direction = direction([1.996, 3.108, -4.554])

  print(vector_direction)

if __name__ == "__main__":
  main()