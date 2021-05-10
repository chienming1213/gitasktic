# Version I 
def miss_num_func(lst):
    "Takes in a list of number and return one missing number"
    return sorted(set(range(lst[0], lst[-1])) - set(lst))