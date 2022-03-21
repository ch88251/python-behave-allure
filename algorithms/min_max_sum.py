def mini_max_sum(arr):
    sums = []
    for num in arr:
        sums.append(sum(arr)-num)
    return min(sums), max(sums)
