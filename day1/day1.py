from collections import defaultdict


def processInput(filename: str) -> list[str]:
    with open(filename) as f:
        data = f.read().splitlines()
    return data

# Part 1
def part1(data: list[str]) -> int:
    ans = 0
    for line in data:
        num = 0
        # Find first digit in line
        for c in line:
            if c.isdigit():
                num = int(c)
                break
        for c in reversed(line):
            if c.isdigit():
                num = num * 10 + int(c)
                break
        ans += num
    return ans

# Part 2
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.value = None


class Trie:
    def __init__(self):
        self.root = TrieNode()
    def add_word(self, word: str, value: int) -> None:
        curr = self.root
        for c in word:
            curr = curr.children[c]
        curr.value = value


number_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digit_words = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
trie = Trie()
reverse_trie = Trie()
for i in range(1, 10):
    trie.add_word(number_words[i-1], i)
    trie.add_word(digit_words[i-1], i)
    reverse_trie.add_word(number_words[i-1][::-1], i)
    reverse_trie.add_word(digit_words[i-1][::-1], i)


def find_num(line: str, trie: Trie) -> int:
    num = None
    for i in range(len(line)):
        curr = trie.root
        for c in line[i:]:
            if c not in curr.children: break
            curr = curr.children[c]
            if curr.value:
                num = curr.value
                break
        if num: break
    return num


def part2(data: list[str]) -> int:
    ans = 0
    for line in data:
        leftnum = find_num(line, trie)
        rightnum = find_num(line[::-1], reverse_trie)
        ans += leftnum * 10 + rightnum
    return ans


if __name__ == "__main__":
    data = processInput("input.txt")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")