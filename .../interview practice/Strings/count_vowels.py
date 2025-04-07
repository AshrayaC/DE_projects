vowel = ['a','e','i','o','u']
word = 'apple'
count = 0
for i in  word:
    if i in vowel:
        count = count + 1
print(count)