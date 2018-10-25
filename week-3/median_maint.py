from typing import List, Tuple
from collections import defaultdict


class Heap(object):
    data: List[int] = []

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

        while True:
            parent_value, parent_pos = self.get_parent(current_pos)
 
            if parent_value > value:
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

    def extract_min(self):
        if len(self.data) == 0:
            return None

        min_value = self.data.pop(0)

        if len(self.data) == 0:
            return min_value

        plucked = self.data.pop()
        self.data.insert(0, plucked)
        current_pos = 0

        while True:
            right_child = self.get_right_child(current_pos)
            left_child = self.get_left_child(current_pos)
            best_swap = None

            if left_child and not right_child:
                best_swap = left_child
            elif not left_child and right_child:
                best_swap = right_child
            elif left_child and right_child:
                best_swap = left_child if left_child[0] < right_child[0] else right_child
            
            if best_swap and best_swap[0] < plucked:
                self.swap_positions(current_pos, best_swap[1])
                current_pos = best_swap[1]
            else:
                break
        
        return min_value


def load_data() -> List[int]:
    numbers = []

    with open('data/numbers.txt', 'r') as f:
        for line in f:
            numbers.append(int(line))

    return numbers


numbers = load_data()

heap = Heap()

heap.insert(9)
heap.insert(4)
heap.insert(12)
heap.insert(11)
heap.insert(13)
heap.insert(4)
heap.insert(4)
heap.insert(8)
heap.insert(9)
heap.insert(1)
heap.insert(3)
heap.insert(20)
heap.insert(7)

print(heap.data)
i = 0


print('Extract min', heap.extract_min(), heap.data)

print('Extract min', heap.extract_min(), heap.data)

print('Extract min', heap.extract_min(), heap.data)

print('Extract min', heap.extract_min(), heap.data)

print('Extract min', heap.extract_min(), heap.data)

print('Extract min', heap.extract_min(), heap.data)

print('Extract min', heap.extract_min(), heap.data)

print('Extract min', heap.extract_min(), heap.data)

print('Extract min', heap.extract_min(), heap.data)

print('Extract min', heap.extract_min(), heap.data)

print('Extract min', heap.extract_min(), heap.data)

print('Extract min', heap.extract_min(), heap.data)

print('Extract min', heap.extract_min(), heap.data)

print('Extract min', heap.extract_min(), heap.data)
