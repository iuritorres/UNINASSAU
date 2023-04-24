if __name__ == '__main__':
  count_interval_1 = 0
  count_interval_2 = 0
  count_interval_3 = 0
  count_interval_4 = 0

  while True:
      num = float(input("Enter a number (or a negative number to stop): "))
      if num < 0:
          break
      if 0 <= num <= 25:
          count_interval_1 += 1
      elif 26 <= num <= 50:
          count_interval_2 += 1
      elif 51 <= num <= 75:
          count_interval_3 += 1
      elif 76 <= num <= 100:
          count_interval_4 += 1

  print("The quantity of numbers in [0-25] is:", count_interval_1)
  print("The quantity of numbers in [26-50] is:", count_interval_2)
  print("The quantity of numbers in [51-75] is:", count_interval_3)
  print("The quantity of numbers in [76-100] is:", count_interval_4)
