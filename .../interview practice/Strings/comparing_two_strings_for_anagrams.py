'''An anagram is a word or phrase formed by rearranging the letters of another word or phrase, using all the original letters exactly once.
For example:
The word "listen" is an anagram of "silent".
The word "earth" is an anagram of "heart".'''

str1 = "Listen"
str2 = "Silent"

str1 = list(str1.upper())
str2 = list(str2.upper())
str1.sort(), str2.sort()

if(str1 == str2):
    print("True")
else:
    print("False")



