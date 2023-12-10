with open("sample.txt") as f:
    lines = [line.rstrip() for line in f]


def score_card(line):
    line = line.split(":")[1]
    winning_nos, ticket_nos = line.split("|")
    winning_nos = set(winning_nos.split())
    ticket_nos = set(ticket_nos.split())
    common_nos = winning_nos & ticket_nos
    if not common_nos:
        score = 0
    else:
        score = 2**(len(common_nos)-1)
    return score


ans = 0
for line in lines:
    score = score_card(line)
    ans += score
print(ans)
