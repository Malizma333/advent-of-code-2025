k = []
while True:
  try:
    k.append(input())
  except EOFError:
    break

start = 0
for i in range(len(k[0])):
  if k[0][i] == "S":
    start = i
    break

seen = {}

def recursive(x, y):
  if (x,y) not in seen:
    if y == len(k):
      value = 1
    elif k[y][x] == "^":
      value = recursive(x+1,y+1) + recursive(x-1,y+1)
    else:
      value = recursive(x,y+1)
    seen[(x,y)] = value
  return seen[(x,y)]

print(recursive(start, 0))
