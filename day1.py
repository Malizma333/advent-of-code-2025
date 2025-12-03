pos = 50
count = 0
while True:
  try:
    spin = input()
    dir = int(spin[0] == "L")*2-1
    for _ in range(int(spin[1:])):
      pos += dir
      pos %= 100
      if pos == 0:
        count += 1
  except EOFError:
    break
print(count)