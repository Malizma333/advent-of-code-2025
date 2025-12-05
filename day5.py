y = []
while True:
  try:
    y.append(input())
  except EOFError:
    break

ranges = []
for x in y:
  if x == "":
    break
  ranges.append(tuple(map(int,x.split("-"))))
ranges.sort()
q = 0
added = []

for item in ranges:
  if len(added) == 0 or item[0] > added[-1][1]:
    added.append([item[0],item[1]])
  else:
    added[-1][1] = max(item[1], added[-1][1])

count = 0
for item in added:
  count += item[1] - item[0] + 1
print(count)