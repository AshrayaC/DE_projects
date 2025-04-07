# You are given a dictionary with a key-value of {string: number} where values in the dictionary could be duplicates. You are required to extract the unique values from the dictionary where the value occurred only once.
#Return a list of values where they occur only once.


# def unique_values(input_dictionary):
#     from collections import Counter

#     #count occurences of values 
#     value_counts = Counter(input_dictionary.values())

#     #filter values that occuer only once
#     unique_values = [val for val, count in value_counts.items() if count ==1]

#     return unique_values


# data = {"a": 1, "b": 2, "c": 2, "d": 3, "e": 4, "f": 4, "g": 5}
# print(unique_values(data))  # Output: [1, 3, 5]


def unique_values(d):
   
    seen_set = set()
    dup_set = set()

    for v in d.values():
        if v in seen_set:
            dup_set.add(v)
        else:
            seen_set.add(v)

    return [v for v in d.values() if v not in dup_set ]




# Example usage:

data = {"a": 1, "b": 2, "c": 2, "d": 3, "e": 4, "f": 4, "g": 5}


print(unique_values(data))  # Output: [1, 3, 5]
# Total Time Complexity = O(n)
# seen_set: In the worst case, all values are unique → size = O(n)

# dup_set: At most all values except one are duplicates → size = O(n)