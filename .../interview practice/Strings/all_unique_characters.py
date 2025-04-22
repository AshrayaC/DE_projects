def all_unique_chars(s: str) -> list:
#     r = []
#     hashmap = {}

#     for char in s:
#         hashmap[char] = hashmap.get(char, 0)+ 1

#     for i, c in hashmap.items():
#        if c == 1:
#           r.append(i)

#     return r  

        

# print(all_unique_chars("leetcode")) 

    seen_set = set()
    dup_set = set()

    for v in s:
        if v in seen_set:
            dup_set.add(v)
        else:
            seen_set.add(v)


    return [''.join(v for v in s if v not in dup_set) ]



print(all_unique_chars('ashdljasaa'))