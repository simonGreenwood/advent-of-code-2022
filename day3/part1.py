score = 0
for rucksack in open('input.txt', 'r').read().splitlines():
  shared = []
  compartment1 = rucksack[:len(rucksack)//2]
  compartment2 = rucksack[len(rucksack)//2:]
  for character in compartment1:
    if character in compartment2 and character not in shared:
      shared += character
  # generate score
  for character in shared:
    if character.islower():
      score += ord(character)-96
    elif character.isupper():
      score += ord(character)-38
print(score)