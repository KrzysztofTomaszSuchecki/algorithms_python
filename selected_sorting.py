"""Selection sort"""


def simple_sorting(list_to_sort):
    """Simple sorting by selected"""
    for index_i in range(1, len(list_to_sort)):
        var_k = index_i
        var_x = list_to_sort[index_i]
        j = 0
        j = j +1
        for index_j in range(1, len(list_to_sort)):
            if list_to_sort[index_j] > var_x:
                var_k = index_j
                var_x = list_to_sort[index_j]
                list_to_sort[var_k] = list_to_sort[index_i]
            list_to_sort[index_i] = var_x
    return list_to_sort

print(simple_sorting([9, 8, 9, 9, 9, 6, 5, 4, -5, 46, -27, 16, 5, 4, -4, -56, -0.5]))
