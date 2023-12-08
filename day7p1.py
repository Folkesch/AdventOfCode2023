file1 = open("inp.txt", "r")
lines = file1.readlines()

file1.close()

for line in range(len(lines)):
  lines[line] = lines[line].strip().split()

def vilkenbombo(cards):
  most_frequent = max(set(cards), key = cards.count)

  if cards[0] == cards[1] == cards[2] == cards[3] == cards[4] == "J":
    for i in range(len(cards)):
      if i + 1 == len(cards):
        cards = cards[:i] + "A"
      else:
        cards = cards[:i] + "A" + cards[i+1:]

  elif most_frequent == "J":
    t = cards
    for i in reversed(range(len(t))):
      if t[i] == "J":
        t = t[:i] + t[i+1:]

    most_frequent = max(set(t), key = t.count)
    for card in range(len(cards)):
      if cards[card] == "J":
        if card + 1 == len(cards):
          cards = cards[:card] + most_frequent
        else:
          cards = cards[:card] + most_frequent + cards[card+1:]

  else:
    for card in range(len(cards)):
      if cards[card] == "J":
        if card + 1 == len(cards):
          cards = cards[:card] + most_frequent
        else:
          cards = cards[:card] + most_frequent + cards[card+1:]

  temp = cards
  temp = "".join(sorted(temp))
  templen = "".join(set(cards))
  if cards[0] == cards[1] == cards[2] == cards[3] == cards[4]:
    return 6
  if temp[0] == temp[1] == temp[2] == temp[3] or temp[4] == temp[1] == temp[2] == temp[3]:
    return 5
  if len(templen) == 2 and ( temp[0] == temp[1] == temp[2] or  temp[2] == temp[3] == temp[4]):
    return 4
  if len(templen) == 3 and ( temp[0] == temp[1] == temp[2] or  temp[2] == temp[3] == temp[4] or temp[2] == temp[3] == temp[1]):
    return 3
  if len(templen) == 3 and ( (temp[0] == temp[1] and temp[2] == temp[3]) or (temp[0] == temp[1] and temp[3] == temp[4]) or (temp[1] == temp[2] and temp[3] == temp[4])):
    return 2
  if len(templen) == 4 and (temp[0] == temp[1] or temp[1] == temp[2] or temp[2] == temp[3] or temp[3] == temp[4]):
    return 1
  return 0


for line in range(len(lines)):
  lines[line].append(vilkenbombo(lines[line][0]))

bol = True

temp = []

while bol == True:
  bol = False
  for line in range(len(lines)):
    if line != len(lines) - 1:
      if lines[line][2] > lines[line+1][2]:
        temp = lines[line]
        lines[line] = lines[line+1]
        lines[line+1] = temp
        bol = True

hash = {"J": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "Q": 12, "K": 13, "A": 14}

bol = True

i = 0

while bol == True:
  bol = False
  for line in range(len(lines)):
    if line != len(lines) - 1:
      if lines[line][2] >= lines[line+1][2] and hash[lines[line][0][0]] > hash[lines[line+1][0][0]]:
        temp = lines[line]
        lines[line] = lines[line+1]
        lines[line+1] = temp
        bol = True
      elif lines[line][2] >= lines[line+1][2] and hash[lines[line][0][0]] == hash[lines[line+1][0][0]]:
        if lines[line][2] >= lines[line+1][2] and hash[lines[line][0][1]] > hash[lines[line+1][0][1]]:
          temp = lines[line]
          lines[line] = lines[line+1]
          lines[line+1] = temp
          bol = True
        elif lines[line][2] >= lines[line+1][2] and hash[lines[line][0][1]] == hash[lines[line+1][0][1]]:
          if lines[line][2] >= lines[line+1][2] and hash[lines[line][0][2]] > hash[lines[line+1][0][2]]:
            temp = lines[line]
            lines[line] = lines[line+1]
            lines[line+1] = temp
            bol = True
          elif lines[line][2] >= lines[line+1][2] and hash[lines[line][0][2]] == hash[lines[line+1][0][2]]:
            if lines[line][2] >= lines[line+1][2] and hash[lines[line][0][3]] > hash[lines[line+1][0][3]]:
              temp = lines[line]
              lines[line] = lines[line+1]
              lines[line+1] = temp
              bol = True
            elif lines[line][2] >= lines[line+1][2] and hash[lines[line][0][3]] == hash[lines[line+1][0][3]]:
              if lines[line][2] >= lines[line+1][2] and hash[lines[line][0][4]] > hash[lines[line+1][0][4]]:
                temp = lines[line]
                lines[line] = lines[line+1]
                lines[line+1] = temp
                bol = True

score = 0

for line in range(len(lines)):
  score += int(lines[line][1]) * (line + 1)

print(score)