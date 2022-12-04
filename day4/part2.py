count = 0
for line in open('input.txt').read().splitlines():
    pair1 = [int(line.split(",")[0].split("-")[0]), int(line.split(",")[0].split("-")[1])]
    pair2 = [int(line.split(",")[1].split("-")[0]), int(line.split(",")[1].split("-")[1])]
    if len(set(range(pair1[0],pair1[1]+1)) & set(range(pair2[0],pair2[1]+1))) > 0:
      count+=1
print(count)