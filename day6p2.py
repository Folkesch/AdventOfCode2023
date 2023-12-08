file1 = open("inp.txt", "r")
lines = file1.readlines()

file1.close()

for line in range(len(lines)):
  lines[line] = lines[line].strip()

for line in range(len(lines)):
  lines[line] = lines[line].split()

time = "53"
lenght = "275"

for i in range(2, len(lines[0])):
  time = time + lines[0][i]
  lenght = lenght + lines[1][i]

time = int(time)
lenght = int(lenght)

score = 0

for t in range(time):
  if (time - t) * t > lenght:
    score += 1

print(score)