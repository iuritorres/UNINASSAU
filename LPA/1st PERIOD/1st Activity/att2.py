if __name__ == '__main__':
  heights = []
  
  for i in range(15):
      height = float(input(f'Insert the {i+1}° height: '))
      heights.append(height)
      
  higher_height = max(heights)
  lower_height = min(heights)

  print(f'Higher height: {higher_height}\nLower height: {lower_height}')
