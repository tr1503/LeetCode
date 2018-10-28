for i in range(len(matrix) * len(matrix[0])):
  print(matrix[i % len(matrix)][i / len(matrix)],end = " ")
