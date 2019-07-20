from functools import reduce
from math import sqrt

def magnitude(vector):

  # Add squared vector numbers

  vector_magnitude = reduce(lambda total, number: total + number ** 2, vector, 0)

  # Calculate the square root

  vector_magnitude = sqrt(vector_magnitude)

  return vector_magnitude