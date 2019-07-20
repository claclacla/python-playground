def check_input_vectors_length(input_vectors):
  length = 0

  for index in range(len(input_vectors)):
    if(index == 0):
      length = len(input_vectors[index])
    else:
      if(len(input_vectors[index]) != length):
        return False

  return True