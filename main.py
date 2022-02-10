from morsekeys import morse_dict

text = input("Write something you want to convert: ").strip()

word_list = text.split()

nested_chars = [list(word.upper()) for word in word_list]

morse_chars = [[morse_dict[char] for char in word] for word in nested_chars]

morse_words = [" ".join(word) for word in morse_chars]

morse_text = "   ".join(morse_words)

print(morse_text)
