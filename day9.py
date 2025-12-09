# k = []
# while True:
#   try:
#     k.append(tuple(map(int, input().split(","))))
#   except EOFError:
#     break
# max_found = 0
# for i in range(len(k)):
#   for j in range(i+1, len(k)):
#     x = abs(k[i][0] - k[j][0]) + 1
#     y = abs(k[i][1] - k[j][1]) + 1
#     if x*y > max_found:
#       max_found = x * y
# print(max_found)

# Part 2: visual searcher with turtle
import turtle

SCALE = 128
k = []
mx, my = 700,300
f = open("input1", "r")
for line in f.readlines():
  k.append(tuple(map(lambda x: int(x)/SCALE, line.split(","))))

turtle.speed(100)
turtle.penup()
turtle.goto(k[-1][0]-mx, k[-1][1]-my)
turtle.pendown()

for i in range(len(k)):
  if i > 0 and abs(k[i][0] - k[i-1][0]) > 100:
    # print the middle
    print(i)
    turtle.pencolor("red")
  else:
    turtle.pencolor("black")
  turtle.goto(k[i][0]-mx,k[i][1]-my)

turtle.pencolor("green")
turtle.fillcolor("green")
turtle.penup()

# Search for a big rectangle
for t in ((249, 250, 400,1), (248,247,100,-1)):
  a = t[0]
  for b in range(t[1], t[2], t[3]):
    turtle.goto(k[a][0]-mx, k[a][1]-my)
    turtle.pendown()
    turtle.goto(k[b][0]-mx, k[a][1]-my)
    turtle.goto(k[b][0]-mx, k[b][1]-my)
    turtle.goto(k[a][0]-mx, k[b][1]-my)
    turtle.goto(k[a][0]-mx, k[a][1]-my)
    turtle.penup()
    x = input()
    if x == "p":
      print(round((SCALE * abs(k[a][0] - k[b][0]) + 1) * (SCALE * abs(k[a][1] - k[b][1]) + 1)))
    if x == "q":
      break
