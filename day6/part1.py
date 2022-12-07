for line in open('example.txt').read().splitlines():
  for i in range(3,len(line)):
    chars = line[i-3:i+1]
    if len(list(set(chars))) == 4:
      print(i+1)
      break