"""A simplified version of how mapreduce works for horizontal scaling"""

from functools import reduce

my_list = [1, 2, 3, 4]

computer1_list = [1, 2]
computer2_list = [3, 4]

# How to find ssv
# Step 1: Square Everything
# Step 2: Sum together

# Traditional way to find Sum of Squared Values
ssv_trad = sum([i ** 2 for i in my_list])  # ssv_trad == 30

# MapReduce
# cp_1_squared_values = map(lambda i: i ** 2, computer1_list)  # computer1_list == [1, 4]
# cp_2_squared_values = map(lambda i: i ** 2, computer2_list)  # computer2_list == [9, 16]


squared_values = map(lambda i: i ** 2, computer2_list)  # computer2_list == [9, 16]


def add_number(x1, x2):
    return x1 + x2


ssv_mapreduce = reduce(add_number, squared_values)
print('Sum of Squared Values (trad)', ssv_trad)
print('Sum of Squared Values (mapreduce)', ssv_mapreduce)