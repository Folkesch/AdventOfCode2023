file1 = open("inp.txt", "r")
lines = file1.readlines()
file1.close()

for line in range(len(lines)):
  lines[line] = lines[line].strip()

Olist = []

linesx = []

for line in range(len(lines)):
  linesx.append(lines[line])
  linesx.append("Ö"*140)
  
linesx = ["Ö"*(len(linesx[0]))] + linesx

for line in range(len(linesx)):
  for i in range(len(linesx[line])):
    linesx[line] = linesx[line][:i*2+1] + "Ö" + linesx[line][i*2+1:]
  

for i in range(len(linesx)):
  linesx[i] = "Ö" + linesx[i]

for i in range(len(linesx)):
  linesx[i] = "N" + linesx[i][1:len(linesx[i]) -2] + "N"

linesx[0] = "N"*len(linesx[0])
linesx[len(linesx)-1] = "N"*len(linesx[len(linesx)-1])

for y in range(len(linesx)-1):
  for x in range(len(linesx[y])-1):
    if linesx[y][x] == "Ö":
      if linesx[y][x+1] in "-J7" and linesx[y][x-1] in "-FL":
        linesx[y] = linesx[y][:x] + "-" + linesx[y][x+1:]
      elif linesx[y+1][x] in "|LJS" and linesx[y-1][x] in "|F7S":
        linesx[y] = linesx[y][:x] + "|" + linesx[y][x+1:]


lines = linesx







y = 0
x = 0
done = False

for line in range(len(lines)):
  for i in range(len(lines[line])):
    if lines[line][i] == "S" and done == False:
      y = line
      x = i
      done = True

done = False
direction = "down"
lenth = 1
y = y + 1

def test(c , b):
  lines[c] = lines[c][:b] + "0" + lines[c][b+1:]

while done == False:

  if lines[y][x] == "S":
    test(y, x)
    break

  if direction == "down":
    if lines[y][x] == "|":
      test(y, x)
      direction = "down"
      y += 1
      lenth += 1
    elif lines[y][x] == "L":
      test(y, x)
      direction = "right"
      x += 1
      lenth += 1
    elif lines[y][x] == "J":
      test(y, x)
      direction = "left"
      x -= 1
      lenth += 1
    else:
      print("dosent Work", y, x, direction)

  elif direction == "right":
    if lines[y][x] == "-":
      test(y, x)
      direction = "right"
      x += 1
      lenth += 1
    elif lines[y][x] == "J":
      test(y, x)
      direction = "up"
      y -= 1
      lenth += 1
    elif lines[y][x] == "7":
      test(y, x)
      direction = "down"
      y += 1
      lenth += 1
    else:
      print("dosent Work", y, x, direction)

  elif direction == "up":
    if lines[y][x] == "|":
      test(y, x)
      direction = "up"
      y -= 1
      lenth += 1
    elif lines[y][x] == "7":
      test(y, x)
      direction = "left"
      x -= 1
      lenth += 1
    elif lines[y][x] == "F":
      test(y, x)
      direction = "right"
      x += 1
      lenth += 1
    else:
      print("dosent Work", y, x, direction)

  elif direction == "left":
    if lines[y][x] == "-":
      test(y, x)
      direction = "left"
      x -= 1
      lenth += 1
    elif lines[y][x] == "L":
      test(y, x)
      direction = "up"
      y -= 1
      lenth += 1
    elif lines[y][x] == "F":
      test(y, x)
      direction = "down"
      y += 1
      lenth += 1
    else:
      print("dosent Work", y, x, direction)

done = False
y = 1
x = 1
lis = []
lis.append([y, x])

def test2(c , b):
  lines[c] = lines[c][:b] + "N" + lines[c][b+1:]

while done == False:
  if lis == []:
    break

  test2(lis[len(lis)-1][0], lis[len(lis)-1][1])

  if lines[lis[len(lis)-1][0]][lis[len(lis)-1][1] + 1] != "0" and lines[lis[len(lis)-1][0]][lis[len(lis)-1][1] + 1] != "N":
    lis.append([lis[len(lis)-1][0], lis[len(lis)-1][1] + 1])
  elif lines[lis[len(lis)-1][0]][lis[len(lis)-1][1] - 1] != "0" and lines[lis[len(lis)-1][0]][lis[len(lis)-1][1] - 1] != "N":
    lis.append([lis[len(lis)-1][0], lis[len(lis)-1][1] - 1])
  elif lines[lis[len(lis)-1][0] + 1][lis[len(lis)-1][1]] != "0" and lines[lis[len(lis)-1][0] + 1][lis[len(lis)-1][1]] != "N":
    lis.append([lis[len(lis)-1][0] + 1, lis[len(lis)-1][1]])
  elif lines[lis[len(lis)-1][0] - 1][lis[len(lis)-1][1]] != "0" and lines[lis[len(lis)-1][0] - 1][lis[len(lis)-1][1]] != "N":
    lis.append([lis[len(lis)-1][0] - 1, lis[len(lis)-1][1]])
  else:
    lis.pop()
      
score = 0

for y in range(1, len(lines), 2):
  for x in range(1, len(lines[y]), 2):
    if lines[y][x] != "Ö" and lines[y][x] != "0" and lines[y][x] != "N":
      score += 1

print(score)