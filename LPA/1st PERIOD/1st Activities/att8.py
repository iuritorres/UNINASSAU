if __name__ == '__main__':
  a = float(input("Enter the initial value of A: "))
  r = float(input("Enter the ratio R: "))

  print("Arithmetic progression:")

  for i in range(10):
      print(a + i*r)
