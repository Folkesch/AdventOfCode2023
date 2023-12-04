file1 = open("inp.txt", "r")
lines = file1.readlines()

for line in lines:
  line = line.strip()

lis = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

tes = ""

test = []


done = False

for line in lines:
  for i in line:
    for j in lis:
      if i == j and done == False:
        tes = i
        done = True
  done = False
  for i in range(len(line)):
    i = len(line) - 1 - i
    for j in lis:
      if line[i] == j and done == False:
        test.append(tes + line[i])
        done = True
  done = False

score = 0

for i in test:
  score += int(i)

print(score)