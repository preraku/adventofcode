from collections import defaultdict


with open("input.txt") as f:
    lines = [line.rstrip() for line in f]


def count_matches(line):
    line = line.split(":")[1]
    winning_nos, ticket_nos = line.split("|")
    winning_nos = set(int(i) for i in winning_nos.split())
    ticket_nos = set(int(i) for i in ticket_nos.split())
    common_nos = winning_nos & ticket_nos
    return len(common_nos)


copies = [1 for _ in range(len(lines))]
for i in range(len(lines)):
    line = lines[i]
    num_matching = count_matches(line)
    for j in range(i + 1, i + 1 + num_matching):
        copies[j] += copies[i] 

print(sum(copies))
