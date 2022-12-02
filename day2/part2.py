score = 0
for line in open('input.txt', 'r').read().splitlines():
  l = line.split(" ")

  if l[1] == 'Z':
    #win so add 6 points
    score += 6
    if l[0] == 'A': 
      score += 2 # to win to rock you need to play paper
    elif l[0] == 'B':
      score += 3 # to win to paper you need to play scissors
    elif l[0] == 'C':
      score += 1 # to win to scissors you need to play rock

  elif l[1] == 'Y':
    #draw so add 3 points
    score += 3
    if l[0] == 'A': # to draw with rock you need to play rock
      score += 1
    elif l[0] == 'B': # draw with paper 
      score += 2
    elif l[0] == 'C': # draw with scissors
      score += 3

  elif l[1] == 'X':
    #loss so add 0 points
    if l[0] == 'A':
      score += 3 # to lose to rock you need to play scissors
    elif l[0] == 'B':
      score += 1 # to lose to paper you need to play rock
    elif l[0] == 'C':
      score += 2 # to lose to scissors you need to play paper
  
print(score)