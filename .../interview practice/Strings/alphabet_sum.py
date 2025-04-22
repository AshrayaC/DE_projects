def words_sum(word):
    total = 0 
    for i in word:
        total = total + ord(i) - ord('a') + 1
    return total



def sum_alphabet(words):

    r = []
    for a in words:
        r.append(words_sum(a))
    return r

# Example usage:
words_list = ["sport", "code", "chatgpt"]
print(sum_alphabet(words_list))  # Output: [88, 27, 75]