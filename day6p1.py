file1 = open("inp.txt", "r")
lines = file1.readlines()

file1.close()

for line in range(len(lines)):
  lines[line] = lines[line].strip()

for line in range(len(lines)):
  lines[line] = lines[line].split()

time = []
lenght = []

for i in range(1, len(lines[0])):
  time.append(int(lines[0][i]))
  lenght.append(int(lines[1][i]))

test = []

for t in range(len(time)):
  test.append([])
  for i in range(time[t]):
    if (time[t] - i) * i > lenght[t]:
      test[t].append(i)

score = 1

for t in test:
  score *= len(t)

print(score)
