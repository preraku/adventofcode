import math

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

time = list(map(int, lines[0].split(':')[1].split()))
distance = list(map(int, lines[1].split(':')[1].split()))

ans = 1
for t, d in zip(time, distance):
    # t and d form a quadratic equation in the form of
    # x^2 - tx + d < 0
    a = 1
    b = -t
    c = d + 0.00000000001

    root1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    root2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)

    temp = root1
    root1 = math.ceil(min(root1, root2))
    root2 = math.floor(max(temp, root2))
    ways = root2 - root1 + 1
    ans *= ways

print(ans)
