grid = []
total = 0
while True:
  try:
    grid.append(list(input()))
  except EOFError:
    break

changed = True
while changed:
  changed = False
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      count = 0
      for dx in range(-1,2):
        for dy in range(-1,2):
          if dx == 0 and dy == 0:
            continue
          if dx+i >= 0 and dy + j >=0 and dx +i < len(grid) and dy + j < len(grid[i]):
            if grid[dx+i][dy+j] == "@":
              count += 1
      if count < 4 and grid[i][j] == "@":
        grid[i][j] = "."
        total += 1
        changed = True
print(total)
