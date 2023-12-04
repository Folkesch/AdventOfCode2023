file1 = open("inp.txt", "r")
lines = file1.readlines()

file1.close()

for line in range(len(lines)):
  lines[line] = lines[line].strip()

def isInt(string):
  try:
    a = int(string)
    return True
  except:
    return False
  
def isCloseto(column, row, length):
  if column == 0:
    if row == 0:
      for j in range(2):
        for i in range(length + 1):
          if lines[j][i] != "." and isInt(lines[j][i]) == False:
            return True
      return False
    
    if (row + length) == len(lines[0]):
      for j in range(2):
        for i in range(row-1, row + length):
          if lines[j][i] != "." and isInt(lines[j][i]) == False:
            return True
      return False
    
    for j in range(2):
      for i in range(row-1, row + length + 1):
        if lines[j][i] != "." and isInt(lines[j][i]) == False:
          return True
    return False
  
  if column + 1 == len(lines):
    if row == 0:
      for j in range(column - 1, column + 1):
        for i in range(length + 1):
          if lines[j][i] != "." and isInt(lines[j][i]) == False:
            return True
      return False
    
    if (row + length) == len(lines[0]):
      for j in range(column - 1, column + 1):
        for i in range(row-1, row + length):
          if lines[j][i] != "." and isInt(lines[j][i]) == False:
            return True
      return False
    
    for j in range(column - 1, column + 1):
      for i in range(row-1, row + length + 1):
        if lines[j][i] != "." and isInt(lines[j][i]) == False:
          return True
    return False
  
  if row == 0:
    for j in range(column - 1, column + 2):
      for i in range(length + 1):
        if lines[j][i] != "." and isInt(lines[j][i]) == False:
          return True
    return False
    
  if (row + length) == len(lines[0]):
    for j in range(column - 1, column + 2):
      for i in range(row-1, row + length):
        if lines[j][i] != "." and isInt(lines[j][i]) == False:
          return True
    return False
   
  for j in range(column - 1, column + 2):
    for i in range(row-1, row + length + 1):
      if lines[j][i] != "." and isInt(lines[j][i]) == False:
        return True
  return False


mysum = []
times_to_wait = 0
score = 0
scorex = 0
scorexx = 0

for line in range(len(lines)):
  for i in range(len(lines[line])):
    if isInt(lines[line][i]):

      if times_to_wait != 0:
        times_to_wait -= 1
      else:
        if i == 138:
          if isInt(lines[line][i + 1]):
            if isCloseto(line, i, 2):
              score += int(lines[line][i:i + 2])
              mysum.append([int(lines[line][i:i + 2]), line, i])
            times_to_wait = 1
          else:
            if isCloseto(line, i, 2):
              score += int(lines[line][i])
              mysum.append([int(lines[line][i]), line, i])
        elif i == 139:
          if isCloseto(line, i, 2):
            score += int(lines[line][i])
            mysum.append([int(lines[line][i]), line, i])
        else:
          if isInt(lines[line][i + 1]):
            if isInt(lines[line][i + 2]):
              if isCloseto(line, i, 3):
                score += int(lines[line][i:i + 3])
                mysum.append([int(lines[line][i:i + 3]), line, i])
              times_to_wait = 2
            elif isInt(lines[line][i + 1]):
              if isCloseto(line, i, 2):
                score += int(lines[line][i:i + 2])
                mysum.append([int(lines[line][i:i + 2]), line, i])
              times_to_wait = 1
          else:
            if isCloseto(line, i, 1):
              score += int(lines[line][i])
              mysum.append([int(lines[line][i]), line, i])
  scorexx = score - scorex
  scorex = score

print(score)

