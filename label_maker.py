import itertools as it
import pprint

list1 = [
    "Title",
]
list2 = [
    "Day 0",
    "Day 1",
]
list3 = [
    "top",
    "middle",
    "bottom",
]

def description_combiner(*args):
    the_list = list(it.product(*args))
    return [",".join(row) for row in the_list]

combined = description_combiner(list1, list2, list3)
pprint.pprint(combined)

def print_combined_descriptions(combined):
    for x in combined:
        print(x)

print_combined_descriptions(combined)
