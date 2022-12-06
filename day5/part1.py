columns = 9
crates=[[] for x in range(columns)]
start = True
for line in open('input.txt').read().splitlines():
  if line[1::4] == "123456789":
    start = False
    crates = list(map(lambda c: c[::-1],crates))
  if start:
    for i in range(columns):
      crates[i].append(line[1::4][i])
      crates[i] = list(filter(lambda x: x != ' ',crates[i]))
  if not start and not line[1::4] == "123456789" and line != "":
    instruction = line.split(" ")
    amount, s, f = int(instruction[1]), int(instruction[3]), int(instruction[5])
    for i in range(amount):
      crates[f-1].append(crates[s-1].pop())
    print(crates)
print("".join([stack[-1] for stack in crates]))