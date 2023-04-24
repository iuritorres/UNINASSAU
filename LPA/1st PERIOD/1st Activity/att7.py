if __name__ == '__main__':
  n = int(input("Enter a value for N (1 to 10): "))

  if n < 1 or n > 10:
      print("Invalid value for N.")

  else:
    
      for i in range(11):
          print(i, " x ", n, " = ", i*n)
