for line in open('input.txt').read().splitlines():
  for i in range(13,len(line)):
    chars = line[i-13:i+1]
    if len(list(set(chars))) == 14:
      print(i+1)
      break