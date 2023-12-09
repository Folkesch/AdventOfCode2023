file1 = open("inp.txt", "r")
lines = file1.readlines()
file1.close()

for line in range(len(lines)):
  lines[line] = lines[line].strip().split()

for line in range(len(lines)):
  for i in range(len(lines[line])):
    lines[line][i] = int(lines[line][i])

temp = [[]]
score = 0

for line in lines:
  for i in line:
    temp[0].append(i)
  
  idx = -1
  done = False
  while done == False:

    done = True
    for i in temp[idx + 1]:
      if i != 0:
        done = False
        break
    if done == True:
      break

    idx = len(temp) - 1
    temp.append([])
    for i in range(len(temp[idx]) - 1):
      temp[idx + 1].append((temp[idx][i + 1] - temp[idx][i]))
  
  tempx = 0
  temp.reverse()
  for i in range(len(temp)):
    tempx += temp[i][len(temp[i]) - 1]
  score += tempx
  temp = [[]]


print(score)