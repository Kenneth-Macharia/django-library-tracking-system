import random
# rand_list =

# list_comprehension_below_10 =

# list_comprehension_below_10 =

# Create a list of 10 random numbers between 1 and 20.
rand_list = [random.randint(1, 19) for _ in range(9)]

# Filter Numbers Below 10 (List Comprehension)
filtered_rand_list_1 = [int for int in rand_list if int < 10]

# Filter Numbers Below 10 (Using filter)
filtered_rand_list_2 = list(
    filter(lambda x: x < 10, rand_list)
)
