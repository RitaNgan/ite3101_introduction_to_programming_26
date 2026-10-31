def median(list: list[int]) -> float:
    sorted_list = sorted(list)
    if len(sorted_list) % 2 == 0: