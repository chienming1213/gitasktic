def miss_num_func2(lst):
    miss=sorted(set(range(lst[0], lst[-1])) - set(lst))
    for i in miss:
        print(i)