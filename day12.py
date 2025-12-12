f = [x[:-1] for x in open("input2").readlines()]
count = 0
for region in f[30:]:
  data = region.split()
  dimensions = tuple(map(int, data[0][:-1].split("x")))
  # :sob:
  count += int(dimensions[0] * dimensions[1] >= sum(map(int, data[1:]))*9)
print(count)
