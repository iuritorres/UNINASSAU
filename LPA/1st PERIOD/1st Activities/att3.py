if __name__ == '__main__':
  accumulated = 0
  qnt_pos = 0
  qnt_neg = 0

  while True:
    number = float(input('Type a number (type 0 to finish program):'))

    if number == 0:
      break
    
    accumulated += number

    if number > 0:
      qnt_pos += 1
    elif number < 0:
      qnt_neg += 1

average = accumulated / (qnt_pos + qnt_neg)
pos_percent = (qnt_pos / (qnt_pos + qnt_neg)) * 100
neg_percent = (qnt_neg / (qnt_pos + qnt_neg)) * 100

print(f'Average: {average:.2f}')
print(f'Positives amount: {qnt_pos}')
print(f'Negative amount: {qnt_neg}')
print(f'Percent positive amount: {pos_percent:.2f}')
print(f'Percent negative amount: {neg_percent:.2f}')
