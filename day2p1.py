file1 = open("inp.txt", "r")
lines = file1.readlines()

for line in range(len(lines)):
  lines[line] = lines[line].strip()

for i in range(len(lines)):
  lines[i] = lines[i].replace(",", "")

blue = 0
red = 0
green = 0

isPos = True
score = 0

for line in lines:
  line = line.split()

  for i in range(2, int(len(line)), 2):
    if line[i+1] == "blue":
      blue += int(line[i])
    elif line[i+1] == "green":
      green += int(line[i])
    elif line[i+1] == "red":
      red += int(line[i])
    elif line[i+1] == "blue;":
      blue += int(line[i])
      if blue > 14 or red > 12 or green > 13:
        isPos = False
      blue = 0
      green = 0
      red = 0
    elif line[i+1] == "green;":
      green += int(line[i])
      if blue > 14 or red > 12 or green > 13:
        isPos = False
      blue = 0
      green = 0
      red = 0
    elif line[i+1] == "red;":
      red += int(line[i])
      if blue > 14 or red > 12 or green > 13:
        isPos = False
      blue = 0
      green = 0
      red = 0
    
    if len(line) == i+2:
      if blue > 14 or red > 12 or green > 13:
        isPos = False
      blue = 0
      green = 0
      red = 0

  if isPos == True:
    if len(line[1]) == 3:
      score += int(line[1][0:2])
    elif len(line[1]) == 4:
      score += int(line[1][0:3])
    else:
      score += int(line[1][0])
  
  isPos = True
    
  

print(score)
