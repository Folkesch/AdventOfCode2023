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


lisx = []
bol = True

for x in range(len(lines[0])):
  for y in range(len(lines)):
    if lines[y][x] == "#" and bol:
      bol = False
  if bol:
    lisx.append(x)
  bol = True


gal = []

for line in range(len(lines)):
  for x in range(len(lines[line])):
    if lines[line][x] == "#":
      gal.append([line, x])

galx = gal.copy()
galx.reverse()

suma = 0

temp = 0

for g in galx:
  for i in range(len(gal)-1):
    suma += abs(abs(gal[i][0] - g[0]) + abs(gal[i][1] - g[1]))
    for x in lisx:
      if (gal[i][1] > x and g[1] < x) or (g[1] > x and gal[i][1] < x):
        suma += 999_999
    for y in lisy:
      if (gal[i][0] > y and g[0] < y) or (g[0] > y and gal[i][0] < y):
        suma += 999_999
  
  gal.pop()

print(suma)