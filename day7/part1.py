current_dir = []
directories = {"/": {}}

for line in open("example.txt").read().splitlines():
  if line.startswith("$ cd"):
    if line[5:] != "..":
      current_dir.append(line[5:])
      print(current_dir)
  elif line == "$ ls":
    print(directories)
  else:
    if line.startswith("dir "):
      print(line[4:])
      print(directories.keys()["/"])
  