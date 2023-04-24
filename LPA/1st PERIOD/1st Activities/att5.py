if __name__ == '__main__':
  sum_all = 0
  sum_even = 0
  count_all = 0
  count_even = 0

  while True:
      num = float(input("Enter a positive number (0 to exit): "))
      if num == 0:
          break

      sum_all += num
      count_all += 1

      if num % 2 == 0:
          sum_even += num
          count_even += 1

  if count_all == 0:
      print("No numbers entered.")

  else:
      average_all = sum_all / count_all
      print("Overall average: ", average_all)
      print("Number of even numbers: ", count_even)

      if count_even == 0:
          print("No even numbers entered.")

      else:
          average_even = sum_even / count_even
          print("Average value of even numbers: ", average_even)

      print("Number of odd numbers: ", count_all - count_even)
