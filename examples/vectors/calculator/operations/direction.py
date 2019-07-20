from .magnitude import *
from .multiply import *

def direction(vector):
  vector_magnitude = magnitude(vector)
  vector_direction = multiply(vector, 1 / vector_magnitude)

  return vector_direction