rucksacks = open('input.txt', 'r').read().splitlines()
count = 0
badges = []
score = 0
for count in range(0,len(rucksacks),3):
  badge = ""
  group = rucksacks[count:count+3]
  for item in group[0]:
    if item in group[1] and item in group[2]:
      badge = item
  badges.append(badge)
print(badges)
for character in badges:
    if character.islower():
      score += ord(character)-96
    elif character.isupper():
      score += ord(character)-38
print(score)