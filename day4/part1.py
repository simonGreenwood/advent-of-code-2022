count = 0
for line in open('input.txt').read().splitlines():
    pair1, pair2 = line.split(",")[0].split("-"), line.split(",")[1].split("-")
    if int(pair1[0]) >= int(pair2[0]) and int(pair1[1]) <= int(pair2[1]) or int(pair1[0]) <= int(pair2[0]) and int(pair1[1]) >= int(pair2[1]):
      count+=1
  
print(count)