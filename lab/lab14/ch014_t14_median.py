from typing import List

def median(list: list[int]) -> float:
    sorted_lst = sorted(lst)
    if len(sorted_list) % 2 == 0:
        index_1 = len(sorted_lst) // 2 - 1
        index_1 = len(sorted_lst) // 2