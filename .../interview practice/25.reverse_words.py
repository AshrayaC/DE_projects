def words_reverse(sentence):
    sentence_list = sentence.split(' ')
    reversed_sentence = ' '.join(reversed(sentence_list))
    return reversed_sentence

print(words_reverse("Hello world!"))  # Output: "world! Hello"