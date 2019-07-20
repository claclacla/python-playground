from functools import reduce
from math import sqrt

def magnitude(vector):

  # Add squared vector numbers

  magnitude = reduce(lambda total, number: total + number ** 2, vector)

  # Calculate the square root

  magnitude = sqrt(magnitude)

  return  magnitude