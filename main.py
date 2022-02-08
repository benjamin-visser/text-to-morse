from morsekeys import morse_dict

test_sentence = "Heya how ya doin my boy"
text = input("Write something you want to convert: ").strip()
# text = test_sentence

word_list = text.split()
print(word_list)

nested_chars = [list(word.upper()) for word in word_list]
print(nested_chars)

morse_chars = [[morse_dict[char] for char in word] for word in nested_chars]
print(morse_chars)

morse_words = [" ".join(word) for word in morse_chars]
print(morse_words)

morse_text = "   ".join(morse_words)
print(morse_text)

