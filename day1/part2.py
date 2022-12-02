# Day 1: Calorie Counting Part 2
count = 0
highs = []
for line in open('input.txt', 'r'):
  if line == '' or line == '\n':
    highs.append(count)
    count = 0
  else:
    count += int(line)
print(sum(sorted(highs)[-3:]))