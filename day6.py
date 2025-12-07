k = []
while True:
  try:
    k.append(list(input()))
  except EOFError:
    break
q = list(map(lambda x:"".join(x), zip(*k)))
first = True
op = ""
current = 0
total = 0
for i in range(len(q)):
  if q[i].strip() == "":
    first = True
    total += current
  elif first:
    op = q[i][-1]
    current = int(q[i][:-1])
    first = False
  else:
    if op == "*":
      current *= int(q[i])
    else:
      current += int(q[i])
print(total + current)
