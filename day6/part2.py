for line in open('input.txt').read().splitlines():
  for i in range(4,len(line)):
    chars = [line[i],line[i-1],line[i-2],line[i-3]]
    if len(list(set(chars))) == 4:
      print(i+1)
      break