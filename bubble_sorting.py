"""Bubble sorting."""

def bubble_sorting(list_to_sort):
    """Boubble sort"""
    for index_i in range(2, len(list_to_sort)):
        set_val = list_to_sort[index_i]
        list_to_sort[0] = set_val
        index_j = index_i - 1
        while set_val < list_to_sort[index_j]:
            list_to_sort[index_j + 1] = list_to_sort[index_j]
            index_j = index_j - 1
        list_to_sort[index_j + 1] = set_val
    return list_to_sort

print(bubble_sorting([345, 22222, 323, 4, 59090, -4354, 4, 4, 4, 4, -444]))
