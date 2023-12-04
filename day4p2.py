file1 = open("inp.txt", "r")
lines = file1.readlines()

file1.close()

for line in range(len(lines)):
  lines[line] = lines[line].strip()

for line in range(len(lines)):
  lines[line] = lines[line].split()

'''
def rem(lis):
  bol = False
  for i in lis:
    if i == " ":
      bol = True
  if bol == False:
    return lis
  else:
    lis.remove(" ")
    return rem(lis)

for line in lines:
  line = rem(line)
'''
  
points = False

winning = [[]]
numbers = [[]]
num = 0

for line in range(len(lines)):
  for i in range(2, len(lines[line])):
    if points:
      winning[line].append(lines[line][i])
    elif lines[line][i] == "|":
      points = True
    else:
      numbers[line].append(lines[line][i])
    
  winning.append([])
  numbers.append([])
  points = False


score = []
for line in lines:
  score.append(1)

sco = 0

for line in range(len(numbers)):
  for i in range(len(numbers[line])):
    for j in range(len(winning[line])):
      if numbers[line][i] == winning[line][j]:
        sco += 1
        break
  if sco == 0:
    sco = 0
  else:
    for i in range(line+1, line + sco+1):
      if i + 1 == len(score):
        score.append(score[line])
      else:
        score[i] += score[line]
    sco = 0
  
print(sum(score))