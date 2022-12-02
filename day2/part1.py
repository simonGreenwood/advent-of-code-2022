score = 0
for line in open('input.txt', 'r').read().splitlines():
  l = line.split(" ")
  if l[1] == 'X':
    score += 1
  elif l[1] == 'Y':
    score += 2
  elif l[1] == 'Z':
    score += 3


  if (l[0] == "A" and l[1] == "Y") or (l[0] == "B" and l[1] == "Z") or (l[0] == "C" and l[1] == "X"):
    score += 6
    print("win")
  elif (l[0] == "A" and l[1] == "X") or (l[0] == "B" and l[1] == "Y") or (l[0] == "C" and l[1] == "Z"):
    score += 3
    print("tie")
  else:
    score += 0
    print("lose")
print(score)