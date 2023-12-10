with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

instructions = [(0 if c == 'L' else 1) for c in lines[0]]

nodes = dict()
currs = []
for line in lines[2:]:
    name, l_r = line.split(' = ')
    l, r = l_r.split('(')[1].split(')')[0].split(',')
    r = r.strip()
    nodes[name] = (l, r)
    if name[-1] == 'A': currs.append(name)
# print((currs))
cycle_lengths = []
for start in currs:
    cycles = 0
    steps = 0
    cycle_points = []
    curr = start
    while True:
        for i in instructions:
            curr = nodes[curr][i]
            steps += 1
            if curr[-1] == 'Z':
                cycles += 1
                cycle_points.append((steps, curr))
                steps = 0
                if cycles == 8:
                    break
        if cycles == 8:
            cycle_lengths.append((start, cycle_points[0][0]))
            print(f"{start}: {cycle_points}")
            break
print(cycle_lengths)
# Find the LCM of the cycle lengths
lengths = [cl[1] for cl in cycle_lengths]

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
def lcm(a, b):
    gcf = gcd(a, b)
    # print(a // gcf)
    return (a // gcf) * b # Need // because py gives a float for / even if the result is an int
from functools import reduce
print(reduce(lcm, lengths))
exit()