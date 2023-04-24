if __name__ == '__main__':
  a = int(input("Enter a positive integer: "))
  result = 1

  for i in range(1, a+1):
      result *= i
      print(i, end="")

      if i < a:
          print(" X ", end="")

      else:
          print(" = ", end="")

  print(result)
