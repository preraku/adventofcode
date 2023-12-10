with open('input.txt', 'r') as f:
    lines = [[int(val) for val in line.strip().split()]
             for line in f.readlines()]

def get_gaps(line):
    return [line[i+1] - line[i] for i in range(len(line) - 1)]


def get_new_num(line):
    gaps = []
    gaps.append(get_gaps(line))
    while not all(i == 0 for i in gaps[-1]):
        last_line = gaps[-1]
        gaps.append(get_gaps(last_line))
    return sum(g[0] for g in gaps) + line[-1]


print(sum(get_new_num(line) for line in lines))
