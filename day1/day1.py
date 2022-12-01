# Day 1: Calorie Counting 
count = 0
high = 0
for line in open('example.txt', 'r').read().splitlines():
    if line == '':
      if count > high:
        high = count
        count = 0
    else: 
      count += int(line)
print(count, high)
    
  