morse_dict = {
    "A": "._",
    "B": "_...",
    "C": "_._.",
    "D": "_..",
    "E": ".",
    "F": ".._.",
    "G": "__.",
    "H": "....",
    "I": "..",
    "J": ".___",
    "K": "_._",
    "L": "._..",
    "M": "__",
    "N": "_.",
    "O": "___",
    "P": ".__.",
    "Q": "__._",
    "R": "._.",
    "S": "...",
    "T": "_",
    "U": ".._",
    "V": "..._",
    "W": ".__",
    "X": "_.._",
    "Y": "_.__",
    "Z": "__..",
    "1": ".____",
    "2": "..___",
    "3": "...__",
    "4": "...._",
    "5": ".....",
    "6": "_....",
    "7": "__...",
    "8": "___..",
    "9": "____.",
    "0": "_____",
    ".": "._._._",
    ",": "__..__",
    ":": "___...",
    "?": "..__..",
    "'": ".____.",
    "-": "_...._",
    "/": "_.._.",
    "(": "_.__._",
    ")": "_.__._",
}
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

