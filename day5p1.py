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

fond = False

temp = 0
tempx = 0

for i in range(len(seds)):
  temp = seds[i]
  for k in sets:
    for j in k:
      if temp >= j[1] and temp <= j[1] + j[2] and fond == False:
        fond = True
        tempx = temp - j[1]
        temp = j[0] + tempx
    fond = False
  seds[i] = temp
  


print(min(seds))