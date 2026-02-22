num = int(input())
unweighted = 0
weight = 0
for _ in range(num):
    letter, tier = list(input().strip())
    letter = letter.upper()
    tier = int(tier)
    if letter == "A":
        unweighted += 4
    elif letter == "B":
        unweighted += 3
    elif letter == "C":
        unweighted += 2
    elif letter == "D":
        unweighted += 1
    if tier == 1 and (letter == "A" or letter == "B" or letter == "C"):
        weight += 0.05
    elif tier == 2 and (letter == "A" or letter == "B" or letter == "C"):
        weight += 0.025
totalGrade = ((unweighted/num) + weight)
print(totalGrade)