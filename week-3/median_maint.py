from typing import List, Tuple
from collections import defaultdict
from operator import lt, gt


class Heap(object):
    data: List[int] = []

    def __init__(self, heap_type: str='min'):
        if heap_type not in ('min', 'max'):
            raise Exception('Must set heap type to min or max')

        self.data = []
        self.type = heap_type

    def size(self):
        return len(self.data)

    def peak_head(self):
        if len(self.data) == 0:
            return None
        return self.data[0]

    def get_parent(self, position: int) -> Tuple[int, int]:
        parent_pos = None

        if position % 2 == 0:
            parent_pos = int(position / 2)
        else:
            parent_pos = int(position/2)

        return self.data[parent_pos], parent_pos

    def insert(self, value: int):
        self.data.append(value)
        current_pos = len(self.data) - 1

        if self.type == 'min':
            comp = gt
        else:
            comp = lt

        while True:
            parent_value, parent_pos = self.get_parent(current_pos)
 
            if parent_value is not None and comp(parent_value, value):
                self.swap_positions(current_pos, parent_pos)
                current_pos = parent_pos
            else:
                break

    def swap_positions(self, one: int, two: int):
        self.data[one], self.data[two] = self.data[two], self.data[one]

    def get_right_child(self, position: int) -> Tuple[int, int]:
        right_pos = (2 * position) + 1

        if len(self.data) > right_pos:
            return (self.data[right_pos], right_pos)
        else:
            return None

    def get_left_child(self, position: int) -> Tuple[int, int]:
        left_pos = 2 * position 
    
        if len(self.data) > left_pos:
            return (self.data[left_pos], left_pos)
        else:
            return None

    def extract(self):
        if len(self.data) == 0:
            return None

        head_value = self.data.pop(0)

        if len(self.data) == 0:
            return head_value

        plucked = self.data.pop()
        self.data.insert(0, plucked)
        self.correct_heap_invarient()
        return head_value

    def correct_heap_invarient(self):
        current_pos = 0
        plucked = self.data[0]

        if self.type == 'min':
            comp = lt
        else:
            comp = gt

        while True:
            right_child = self.get_right_child(current_pos)
            left_child = self.get_left_child(current_pos)
            best_swap = None

            if left_child and not right_child:
                best_swap = left_child
            elif not left_child and right_child:
                best_swap = right_child
            elif left_child and right_child:
                best_swap = left_child if comp(left_child[0], right_child[0]) else right_child
            
            if best_swap and comp(best_swap[0], plucked):
                self.swap_positions(current_pos, best_swap[1])
                current_pos = best_swap[1]
            else:
                break


def load_data() -> List[int]:
    numbers = []

    with open('data/numbers.txt', 'r') as f:
        for line in f:
            numbers.append(int(line.strip()))

    return numbers


heap_left = Heap('max')
heap_right = Heap('min')
medians = []

for num in load_data():
    current_median: int = None

    if heap_left.peak_head() is None or num >= heap_left.peak_head():
        heap_right.insert(num)
    else:
        heap_left.insert(num)

    while heap_left.size() > 0 and heap_left.size() > heap_right.size():
        shift_value = heap_left.extract()
        heap_right.insert(shift_value)
    
    while heap_right.size() > 0 and heap_right.size() - 1 > heap_left.size():
        shift_value = heap_right.extract()
        heap_left.insert(shift_value)

    if (heap_left.size() + heap_right.size()) % 2 == 0:
        current_median = heap_left.peak_head()
    else:
        current_median = heap_right.peak_head()

    medians.append(current_median)
    

print('Answer:', sum(medians) % 10000)
