def first_non_repeating_character(s):
    for i in s:
        if s.count(i) == 1:
            return i
    return None

print(first_non_repeating_character("swiss"))