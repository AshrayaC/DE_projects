def all_unique_chars(s: str) -> list:
    r = []
    hashmap = {}

    for char in s:
        hashmap[char] = hashmap.get(char, 0)+ 1

    for i, c in hashmap.items():
       if c == 1:
          r.append(i)

    return r  

        

print(all_unique_chars("leetcode")) 

