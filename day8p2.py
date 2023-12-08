file1 = open("inp.txt", "r")
lines = file1.readlines()
file1.close()

for line in range(len(lines)):
  lines[line] = lines[line].strip().replace("(", "").replace(")", "").replace(",", "").replace("=", "").split()


lrlr = lines[0]

inplis = lines[2:].copy()

test = []

for i in range(len(inplis)):
  if inplis[i][0][2] == "A":
    test.append([i, inplis[i][0]])

done = False
tofind = ""
curentAAA = test[0][0]
steps = 0
info = [[]]

for k in range(len(test)):
  curentAAA = test[k][0]
  while done == False:
    for i in range(len(lrlr[0])):
      if lrlr[0][i] == "L":
        tofind = inplis[curentAAA][1]
        steps += 1

        for z in info[k]:
          if z[1] == i and z[2] == tofind:
            done = True
            info[k].append([steps, i, tofind])
            break

        if tofind[2] == "Z":
          info[k].append([steps, i, tofind])
        

        for j in range(len(inplis)):
          if inplis[j][0] == tofind:
            curentAAA = j 
            break
      else:
        tofind = inplis[curentAAA][2]
        steps += 1

        for z in info[k]:
          if z[1] == i and z[2] == tofind:
            done = True
            info[k].append([steps, i, tofind])
            break

        if tofind[2] == "Z":
          info[k].append([steps, i, tofind])

        for j in range(len(inplis)):
          if inplis[j][0] == tofind:
            curentAAA = j 
            break

  steps = 0
  done = False
  info.append([])

for i in range(len(info)-1):
  info[i].pop()
      
score = []

for i in range(len(info)-1):
  score.append(info[i][0][0] - info[i][1][0])

import math

print(math.lcm(score[0], score[1], score[2], score[3], score[4], score[5]))