from typing import List, Tuple
from collections import defaultdict
from operator import lt, gt


def load_data() -> List[int]:
    numbers = []
    seen = {}

    with open('data/numbers.txt', 'r') as f:
        for line in f:
            num = int(line.strip())
            if num in seen:
                continue
            seen[num] = 1
            numbers.append(num)

    return numbers

numbers = load_data()
hashed = {n: 1 for n in numbers}
count = 0

for t in range(-10000,10001):
    for num in numbers:
        requires = t - num
        if hashed.get(requires):
            count = count + 1
            print('Found:', count)
            break

print('Final count:', count)
