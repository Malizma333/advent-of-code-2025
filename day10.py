import itertools
import sympy as sp

f = [x.strip() for x in open("input2").readlines()]
count = 0

def calc(query):
  target = list(map(int,query[-1][1:-1].split(",")))
  button_wiring = list(map(lambda x:list(map(int,x[1:-1].split(","))), query[1:-1]))
  buttons = [[int(j in button) for j in range(len(target))] for button in button_wiring]
  # range of values free variables can take
  max_button_presses = [min(target[l] for l in button) for button in button_wiring]
  # Ax = B
  # A is what each button increments
  # x is the amount of times each button is pressed
  # B is the target jolt values
  # know A and B, solve for x
  formula_matrix = list(zip(*(buttons + [target])))
  # Get in reduced echelon form
  result, pivots = sp.Matrix(formula_matrix).rref()
  free_indices = set(range(len(buttons))).difference(set(pivots))
  free_maxes = []
  for i in range(len(buttons)):
    if i in free_indices:
      free_maxes.append(max_button_presses[i] + 1)
    else:
      free_maxes.append(1)
  lowest = 1000000

  # Iterate through free variable combinations to find all possible solutions
  for free_values in itertools.product(*map(range, free_maxes)):
    weights = []
    c = 0
    valid = True
    for i in range(len(buttons)):
      if i in free_indices:
        weights.append(free_values[i])
      else:
        total = result[c,-1]
        for j in free_indices:
          total += -result[c,j] * free_values[j]
        if total < 0 or total % 1 != 0:
          valid = False
          break
        weights.append(total)
        c += 1
    if valid:
      lowest = min(lowest, sum(weights))
  return lowest

count = 0
for i in range(len(f)):
  total = calc(f[i].split())
  count += total

print(count)

# part 1 approach was something like this but not exactly
# import heapq
# 
# f = [x.strip() for x in open("input2").readlines()]
# 
# for query, i in enumerate(f):
#   target_jolt = list(map(int,query[-1][1:-1].split(",")))
#   button_wiring = list(map(lambda x:list(map(int,x[1:-1].split(","))), query[1:-1]))
#   buttons = np.array([[int(j in button) for j in range(len(target_jolt))] for button in button_wiring]).transpose()
#   queue = [sum(target_jolt), , 0]
#   heapq.heapify(queue)
#   visited = set()
#   while queue:
#     (closeness, current, depth) = heapq.heappop(queue)
#     if tuple(current) in visited:
#       continue
#     visited.add(tuple(current))
#     if all(current[i] == target[i] for i in range(len(target))):
#       return depth
#     for button in button_wiring:
#       copy_current = [*current]
#       copy_closeness = closeness
#       for element in button:
#         copy_current[element] += 1
#         copy_closeness -= 1
#         if copy_current[element] > target[element]:
#           break
#       else:
#         heapq.heappush(queue, (copy_closeness, copy_current, depth + 1))
# 
# count = 0
# for i in range(len(f)):
#   count += calc(f[i].split())
# 
# print(count)