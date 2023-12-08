file1 = open("inp.txt", "r")
lines = file1.readlines()

file1.close()

for line in range(len(lines)):
  lines[line] = lines[line].strip().replace("(", "").replace(")", "").replace(",", "").replace("=", "").split()


lrlr = lines[0]

inplis = lines[2:]

done = False
kidex = 0
asteps = 0
tofind = ""
score = 0

for line in range(len(inplis)):
  if inplis[line][0] == "AAA":
    kindx = line
    break


while done == False:
  for i in lrlr[0]:
    if i == "L":
      tofind = inplis[kindx][1]
      asteps += 1

      if tofind == "ZZZ":
        done = True
        score = asteps
        break

      for line in range(len(inplis)):
        if inplis[line][0] == tofind:
          kindx = line
          break
    else:
      tofind = inplis[kindx][2]
      asteps += 1

      if tofind == "ZZZ":
        done = True
        score = asteps
        break

      for line in range(len(inplis)):
        if inplis[line][0] == tofind:
          kindx = line
          break

print(score)