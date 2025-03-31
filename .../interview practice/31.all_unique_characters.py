def all_unique_chars(s: str) -> list:
    hashmap = {}
    r = []
    # Count occurrences of each character
    for i in s:
        hashmap[i] = hashmap.get(i, 0) + 1

    # Collect all unique characters
    for k , y in hashmap.items():
        if y == 1:
            r.append(k)
    '''unique_chars = [i for i in s if hashmap[i] == 1]'''
    return r  # Returns a list of all unique characters

print(all_unique_chars("leetcode")) 