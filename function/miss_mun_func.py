
def miss_num_func(lst):
    return sorted(set(range(lst[0], lst[-1])) - set(lst))