import re
from collections import defaultdict

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

# (row, col) -> set of (number: int, line_no: int, idx_of_first_digit: int)
stars_to_nums = defaultdict(set)
# Store all stars' coordinates as the keys
for i in range(len(lines)):
    for match in re.finditer(r'\*', lines[i]):
        stars_to_nums[(i, match.start())] = set()


def findNum(line: int, idx: int, star_idx: tuple[int, int]) -> None:
    # Given an index (line, idx), check if digit. If so, expand to find the number and add to set
    # until you reach a non digit character. Then, add to stars_to_nums
    if line < 0 or line >= len(lines):
        return
    if idx < 0 or idx >= len(lines[line]):
        return
    if not lines[line][idx].isdigit():
        return
    start_idx = idx
    # Expand to left
    while start_idx >= 0 and lines[line][start_idx].isdigit():
        start_idx -= 1
    start_idx += 1
    # Expand to right
    end_idx = idx
    while end_idx < len(lines[line]) and lines[line][end_idx].isdigit():
        end_idx += 1
    end_idx -= 1
    # Add the number to the set
    num = int(lines[line][start_idx:end_idx + 1])
    stars_to_nums[star_idx].add((num, line, start_idx))


# For each star, explore all 8 directions and find all the numbers
for star_row, star_col in stars_to_nums.keys():
    for row in range(star_row - 1, star_row + 2):
        for col in range(star_col - 1, star_col + 2):
            if row == star_row and col == star_col:
                continue
            findNum(row, col, (star_row, star_col))

# For each star in the dictionary with exactly 2 numbers, multiply them and add to the answer
ans = 0
for star_idx, nums in stars_to_nums.items():
    if len(nums) == 2:
        num1, num2 = nums
        ans += num1[0] * num2[0]

print(ans)
