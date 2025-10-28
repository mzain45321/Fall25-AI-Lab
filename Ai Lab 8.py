# Min=Max Algorithm
import math
values = [3, 2, 5, 4, 7, 2, 7, 7]
levels = math.log(len(values), 2)

def min_max(curr_depth, node_index, min_turn, values, tree_depth):
    if curr_depth == tree_depth:
        return values[node_index]
    if (min_turn):
        return min(min_max(curr_depth + 1, node_index*2, False, values, tree_depth),
                   min_max(curr_depth + 1, node_index*2+1, False, values, tree_depth))
    else:
        return max(min_max(curr_depth + 1, node_index*2, True, values, tree_depth),
                   min_max(curr_depth + 1, node_index*2+1, True, values, tree_depth))

print(min_max(0, 0, True, values, levels))