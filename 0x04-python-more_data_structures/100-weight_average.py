#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        upper = 0
        lower = 0
        for num in my_list:
            upper += (num[0] * num[1])
            lower += (num[1])
        return (upper/lower)
    return 0
