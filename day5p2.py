file1 = open("inp.txt", "r")
lines = file1.readlines()

file1.close()

for line in range(len(lines)):
  lines[line] = lines[line].strip()

for line in range(len(lines)):
  lines[line] = lines[line].split()

def isInt(string):
  try:
    a = int(string)
    return True
  except:
    return False

seds = []
sets = [[], [], [], [], [], [], []]

index = -1

for line in lines:
  if line != []:
    if line[0] == "seeds:":
      for i in range(1,len(line)):
        seds.append(int(line[i]))
    elif isInt(line[0]) == False:
      index += 1
    else:
      sets[index].append([int(line[0]), int(line[1]), int(line[2])])

done = False

numli = []
temp = []
tempx = 0
score = []

for i in range(0 ,len(seds), 2):
  numli = [[seds[i], (seds[i] + seds[i+1])]]
  for block in sets:
    for inp in block:
      for k in range(len(numli)):
        if inp[1] < numli[k][0] and inp[1] + inp[2] > numli[k][1]:
          temp.append([inp[0] + (numli[k][0] - inp[1]), inp[0] + (numli[k][1] - inp[1])])
          numli[k].clear()

        elif inp[1] < numli[k][0] and inp[1] + inp[2] > numli[k][0]:
          temp.append([inp[0] + (numli[k][0] - inp[1]), inp[0] + inp[2]])
          numli[k] = [inp[1] + inp[2] + 1, numli[k][1]]
          
        elif inp[1] < numli[k][1] and inp[1] + inp[2] > numli[k][1]:
          temp.append([inp[0], inp[0] + numli[k][1] - inp[1]])
          numli[k] = [numli[k][0], inp[1]-1]
          
        elif inp[1] > numli[k][0] and inp[1] + inp[2] < numli[k][1]:
          temp.append([inp[0], inp[0], inp[2]])
          numli.append([inp[1] + inp[2] + 1, numli[k][1]])
          numli[k] = [numli[k][0], inp[1]-1]
      
      a = []
      for z in range(len(numli)):
        if numli[z] == []:
          a.append(z)
      a.reverse()
      for z in a:
        numli.pop(z)

    numli.extend(temp)
    temp.clear()

  for f in numli:
    score.append(f[0])


print(min(score))