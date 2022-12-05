crates=[[],[],[]]
for line in open('example.txt').read().splitlines():
  positions = list(range(1,34,4))
  for i in range(0,3):
    crates[i].append(line[positions[i]:positions[i]+4])
print(list(map(lambda x: x.replace(" ","").replace("]","").replace("[",""),crates)))