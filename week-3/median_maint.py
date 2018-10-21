from typing import List, Tuple
from collections import defaultdict


def load_data() -> List[int]:
    numbers = []

    with open('data/numbers.txt', 'r') as f:
        for line in f:
            numbers.append(int(line))

    return numbers


numbers = load_data()
