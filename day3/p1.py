import re

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

all_nums = []
for i in range(len(lines)):
    # Collect numbers in this line (separated by any non digit character) into a list along with length and character number
    # e.g. 467..114.. -> [(467, 3, 0), (114, 3, 5)]
    nums = []
    for match in re.finditer(r'(\d+)', lines[i]):
        num = match.group(1)
        length = len(num)
        idx = match.start()
        nums.append((int(num), length, idx))
    all_nums.append(nums)
# print(all_nums)

def checkForSymbols(line: int, start: int, end: int) -> bool:
    # print(line, start, end)
    if line < 0 or line >= len(lines):
        return False
    for i in range(start, end+1):
        if i < 0 or i >= len(lines[line]):
            continue
        char = lines[line][i]
        if char != '.' and not char.isdigit():
            return True
    return False


ans = 0
for i in range(len(all_nums)):
    for num, length, idx in all_nums[i]:
        # print(num, length, idx)
        # Check if the num is surrounded in the previous line, current line, or next line
        # by a "symbol". A symbol is a character which is not a digit or a period.

        # If it is touching a symbol it is a valid number. Add it to ans. Else, continue to the next num.
        start = idx - 1
        end = idx + length
        for row in range(i-1, i+2):
            if checkForSymbols(row, start, end):
                ans += num
                break

print(ans)
