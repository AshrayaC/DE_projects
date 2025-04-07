def words_reverse(sentence):
    sentence_list = sentence.split(' ')
    print(sentence_list)
    reversed_sentence = ' '.join(reversed(sentence_list))
    print(reversed_sentence)
    return reversed_sentence

print(words_reverse("Hello world!"))  # Output: "world! Hello"