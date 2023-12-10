file1 = open("inp.txt", "r")
lines = file1.readlines()
file1.close()

for line in range(len(lines)):
  lines[line] = lines[line].strip()


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

while done == False:

  if lines[y][x] == "S":
    
    break

  if direction == "down":
    if lines[y][x] == "|":
      direction = "down"
      y += 1
      lenth += 1
    elif lines[y][x] == "L":
      direction = "right"
      x += 1
      lenth += 1
    elif lines[y][x] == "J":
      direction = "left"
      x -= 1
      lenth += 1
    else:
      print("does not Work", y, x, direction)

  elif direction == "right":
    if lines[y][x] == "-":
      direction = "right"
      x += 1
      lenth += 1
    elif lines[y][x] == "J":
      direction = "up"
      y -= 1
      lenth += 1
    elif lines[y][x] == "7":
      direction = "down"
      y += 1
      lenth += 1
    else:
      print("does not Work", y, x, direction)

  elif direction == "up":
    if lines[y][x] == "|":
      direction = "up"
      y -= 1
      lenth += 1
    elif lines[y][x] == "7":
      direction = "left"
      x -= 1
      lenth += 1
    elif lines[y][x] == "F":
      direction = "right"
      x += 1
      lenth += 1
    else:
      print("does not Work", y, x, direction)

  elif direction == "left":
    if lines[y][x] == "-":
      direction = "left"
      x -= 1
      lenth += 1
    elif lines[y][x] == "L":
      direction = "up"
      y -= 1
      lenth += 1
    elif lines[y][x] == "F":
      direction = "down"
      y += 1
      lenth += 1
    else:
      print("does not Work", y, x, direction)

print(lenth/2)