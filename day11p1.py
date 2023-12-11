file1 = open("inp.txt", "r")
lines = file1.readlines()
file1.close()

for line in range(len(lines)):
  lines[line] = lines[line].strip()

bol = True
lisy = []

for line in range(len(lines)):
  for i in range(len(lines[line])):
    if lines[line][i] == "#" and bol:
      bol = False
  if bol:
    lisy.append(line)
  bol = True

tal = 0

for line in lisy:
  lines = lines[:line+tal] + ["."*len(lines[0])] + lines[line+tal:]
  tal += 1

lisx = []
bol = True

for x in range(len(lines[0])):
  for y in range(len(lines)):
    if lines[y][x] == "#" and bol:
      bol = False
  if bol:
    lisx.append(x)
  bol = True

tal = 0

for x in lisx:
  for y in range(len(lines)):
    lines[y] = lines[y][:x+tal] + "." + lines[y][x+tal:]
  tal += 1


gal = []

for line in range(len(lines)):
  for x in range(len(lines[line])):
    if lines[line][x] == "#":
      gal.append([line, x])

galx = gal.copy()
galx.reverse()

suma = 0

for g in galx:
  for i in range(len(gal)-1):
    suma += abs(abs(gal[i][0] - g[0]) + abs(gal[i][1] - g[1]))
  
  gal.pop()

print(suma)