with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

instructions = [(0 if c == 'L' else 1) for c in lines[0]]

nodes = dict()
for line in lines[2:]:
    name, l_r = line.split(' = ')
    l, r = l_r.split('(')[1].split(')')[0].split(',')
    r = r.strip()
    nodes[name] = (l, r)

curr, dest = 'AAA', 'ZZZ'
steps = 0
while True:
    for i in instructions:
        if i == 0:
            curr = nodes[curr][0]
        else:
            curr = nodes[curr][1]
        steps += 1
        if curr == dest:
            print(steps)
            exit()

