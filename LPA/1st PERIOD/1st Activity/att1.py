if __name__ == '__main__':
  accumulated = 0
  
  for number in range(0, 501, 3):
      if number % 2 != 0:
          accumulated += number
          
  print(accumulated)
