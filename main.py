if __name__ == "__main__":
  # Introduction to Python list comprehensions

  numbers = [1, 2, 3, 4, 5]
  print(numbers)

  squares = []
  for number in numbers:
    squares.append(number ** 2)
  print(squares)

  numbers = [1, 2, 3, 4, 5]
  print(numbers)

  squares = list(map(lambda number: number ** 2, numbers))
  print(squares)

  numbers = [1, 2, 3, 4, 5]
  print(numbers)

  squares = [number ** 2 for number in numbers]
  print(squares)

  """
  [output_expression for element in list]
  """
