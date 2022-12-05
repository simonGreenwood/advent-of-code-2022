columns = 3
crates=[[] for x in range(columns)]
start = True
for line in open('example.txt').read().splitlines():
  if line[1::4] == "123":
    start = False
    crates = list(map(lambda c: c[::-1],crates))
  if start:
    for i in range(columns):
      crates[i].append(line[1::4][i])
      crates[i] = list(filter(lambda x: x != ' ',crates[i]))
  if not start and not line[1::4] == "123" and line != "":
    instruction = line.split(" ")
    amount, s, f = int(instruction[1]), int(instruction[3]), int(instruction[5])
    print(amount, s, f)
print(crates)