total = 0
while True:
  try:
    batteries = [int(i) for i in input()]
    total = 12
    number = batteries[:total]
    for i in range(len(batteries)-total+1):
      for j in range(total):
        if batteries[i+j] > number[j] and i+total-1 < len(batteries):
          number = number[0:j] + batteries[i+j:i+total]
    total += sum(number[i]*10**(total - i - 1) for i in range(total))
  except EOFError:
    break
print(total)