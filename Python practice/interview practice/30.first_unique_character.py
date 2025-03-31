def first_unique_char(s: str) -> str:
    hashmap = {}
    
    # Count occurrences of each character
    for i in s:
        hashmap[i] = hashmap.get(i, 0) + 1

    # Find the first unique character
    for i in s:
        if hashmap[i] == 1:
            return i  # Return the character itself
    
    return None  # If no unique character is found
print(first_unique_char("leetcode"))  # Output: "l"