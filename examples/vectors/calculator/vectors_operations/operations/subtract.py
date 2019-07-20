from functools import reduce

from ..lib.check_input_vectors_length import *

def _subtract_vectors(vector1, vector2):
  for index in range(len(vector1)):
    vector1[index] -= vector2[index]

  return vector1

def subtract(input_vectors):
  if(not check_input_vectors_length(input_vectors)):
    raise Exception("Subtraction error: The input vectors haven't the same length")

  output = reduce(_subtract_vectors, input_vectors)

  return output