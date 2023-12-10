with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

colors = {
    "red": 12,
    "green": 13,
    "blue": 14
}

# 12 red cubes, 13 green cubes, and 14 blue cubes
ans = 0
for line in lines:
    # Game 3: 4 blue, 4 green; 2 green, 2 blue; 8 green, 2 red, 3 blue
    game, draws = line.split(":")
    draws = draws.split(";")
    valid = True
    for draw in draws:
        counts_and_colors = draw.split(",")
        for count_and_color in counts_and_colors:
            count, color = count_and_color.split()
            if int(count) > colors[color]:
                valid = False
                break
        if not valid:
            break
    if valid:
        ans += int(game.split()[1])
print(ans)
