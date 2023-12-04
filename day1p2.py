file1 = open("inp.txt", "r")
lines = file1.readlines()

for line in range(len(lines)):
  lines[line] = lines[line].strip()

lis = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",]
liss = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

hash = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

tes = ""

test = []


done = False

for line in lines:
  for i in range(len(line)):
    for j in lis:
      if line[i] == j and done == False:
        tes = line[i]
        done = True
    for j in liss:
      if line[i:(i + len(j))] == j and done == False:
        tes = hash[j]
        done = True
  
  done = False
  for i in range(len(line)):
    i = len(line) - i - 1
    for j in lis:
      if line[i] == j and done == False:
        test.append(tes + line[i])
        done = True
    for j in liss:
      if len(line) - i >= len(j):
        if line[i:(i + len(j))] == j and done == False:
          test.append(tes + hash[j])
          done = True
  done = False


score = 0

for i in test:
  score += int(i)

print(score)