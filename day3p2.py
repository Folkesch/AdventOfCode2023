file1 = open("inp.txt", "r")
lines = ["............................................................................................................................................"]
lines.extend(file1.readlines())
lines.append("............................................................................................................................................")

for line in lines:
  line = "." + line + "."

file1.close()

for line in range(len(lines)):
  lines[line] = lines[line].strip()

def isInt(string):
  try:
    a = int(string)
    return True
  except:
    return False

indOfTemp = []


def indexOfInt(column, row):
  if isInt(lines[column][row-1]):
    if isInt(lines[column][row-2]):
      return [(row - 2), row]
    else:
      IntStart = row - 1
  else:
    IntStart = row
  
  if isInt(lines[column][row+1]):
    if isInt(lines[column][row+2]):
      return [row, (row + 2)]
    else:
      IntEnd = row + 1
  else:
    IntEnd = row
  
  return [IntStart, IntEnd]

dupTemp = []

def removeDup(lista):
  dupTemp.clear()
  for i in range(len(lista)):
    for j in range(len(lista)):
      if i != j:
        if lista[i][0] == lista[j][0] and lista[i][1] == lista[j][1] and lista[i][2] == lista[j][2]:
          dupTemp.append(i)
  if len(dupTemp) == 0:
    return lista
  else:
    lista.pop(dupTemp[0])
    return removeDup(lista)




def gear(column, row):
  gearTemp = []
  tem = []
  for i in range(column - 1, column + 2):
    for j in range(row - 1, row + 2):
      if isInt(lines[i][j]):
        tem = indexOfInt(i, j)
        gearTemp.append([i, tem[0], tem[1]])
  gearTemp = removeDup(gearTemp)
  if len(gearTemp) == 2:
    return int(lines[gearTemp[0][0]][gearTemp[0][1]:gearTemp[0][2]+1]) * int(lines[gearTemp[1][0]][gearTemp[1][1]:gearTemp[1][2]+1])
  else:
    return 0
  


mysum = []
temp = []

for line in range(len(lines)):
  for i in range(len(lines[line])):
    if lines[line][i] == "*":
      mysum.append(gear(line, i))

print(sum(mysum))