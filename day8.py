k = []
while True:
  try:
    k.append(tuple(map(int, input().split(","))))
  except EOFError:
    break

def dist(t1,t2):
  return (t1[0]-t2[0])**2 + (t1[1]-t2[1])**2 + (t1[2]-t2[2])**2

distances = []
for i in range(len(k)):
  for j in range(i+1, len(k)):
    distances.append((dist(k[i], k[j]),i,j))
distances.sort(reverse=True)

parents = [-1 for _ in range(len(k))]
group_counts = [1 for _ in range(len(k))]
count = 0

for item in distances[::-1]:
  print(item[0], k[item[1]], k[item[2]])

while count < len(k)-1:
  _, i, j = distances.pop()
  a,b = k[i], k[j]
  while parents[i] != -1:
    i = parents[i]
  while parents[j] != -1:
    j = parents[j]
  if i != j:
    count += 1
    if count == len(k)-1:
      print(a[0]*b[0])
    if i < j:
      parents[i] = j
      group_counts[j] += group_counts[i]
    else:
      parents[j] = i
      group_counts[i] += group_counts[j]

group_counts.sort()
print(group_counts[-3:])