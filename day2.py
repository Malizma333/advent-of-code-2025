ranges = list(map(lambda x: list(map(int,x.split("-"))), input().split(",")))
count = 0
for r in ranges:
  for number in range(r[0], r[1]+1):
    str_number = str(number)
    size = len(str_number)
    bad_number = False
    for m in range(1, size//2 + 1):
      for k in range(0, size - m, m):
        bad_number = True
        q1 = str_number[k:k+m]
        q2 = str_number[k+m:k+2*m]
        if q1 != q2:
          bad_number = False
          break
      if bad_number:
        count += number
        break
print(count)
