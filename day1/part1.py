# Day 1: Calorie Counting Part 1
count = 0
high = 0
for line in open('input.txt', 'r'):
  if line == '' or line == '\n':
    if count>high:
      high = count
    count = 0
  else:
    count += int(line)
print(high)