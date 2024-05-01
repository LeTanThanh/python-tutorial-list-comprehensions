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

  # Python list comprehension with if condition

  mountains = [
    ["Makalu", 8485],
    ["Lhotse", 8516],
    ["Kanchendzonga", 8586],
    ["K2", 8611],
    ["Everest", 8848]
  ]
  print(mountains)

  highest_mountains = list(filter(lambda mountain: mountain[1] > 8_600, mountains))
  print(highest_mountains)

  """
  [output_expression for element in list if condition]
  """

  mountains = [
    ["Makalu", 8485],
    ["Lhotse", 8516],
    ["Kanchendzonga", 8586],
    ["K2", 8611],
    ["Everest", 8848]
  ]
  print(mountains)

  highest_mountains = [mountain for mountain in mountains if mountain[1] > 8600]
  print(highest_mountains)
