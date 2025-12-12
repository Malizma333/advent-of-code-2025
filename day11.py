f = [x.strip() for x in open("input2").readlines()]
devices = {}
incoming = {"svr": 0}
for line in f:
  a,b = line.split(":")
  devices[a] = b.strip().split(" ")
  for item in devices[a]:
    incoming[item] = incoming.get(item, 0) + 1

start = "svr"
queue = [start]
device_count = {start: (1,0,0,0)}
while queue:
  current = queue.pop()
  if current == "out":
    break
  for device in devices[current]:
    incoming[device] -= 1
    if incoming[device] == 0:
      queue.append(device)
    is_fft = device == "fft"
    is_dac = device == "dac"
    current_amounts = device_count[current]
    device_amounts = list(device_count.get(device, (0,0,0,0)))
    if not is_fft and not is_dac:
      device_amounts[0] += current_amounts[0]
      device_amounts[1] += current_amounts[1]
      device_amounts[2] += current_amounts[2]
      device_amounts[3] += current_amounts[3]
    elif not is_fft and is_dac:
      device_amounts[0] = 0
      device_amounts[1] += current_amounts[1] + current_amounts[0]
      device_amounts[2] = 0
      device_amounts[3] += current_amounts[3] + current_amounts[2]
    elif is_fft and not is_dac:
      device_amounts[0] = 0
      device_amounts[1] = 0
      device_amounts[2] += current_amounts[2] + current_amounts[0]
      device_amounts[3] += current_amounts[3] + current_amounts[1]
    device_count[device] = tuple(device_amounts)

print(device_count["out"])