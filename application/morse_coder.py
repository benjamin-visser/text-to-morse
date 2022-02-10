import json

with open("application/morse-dictionary.json", "r") as f:
    morse_dict = json.load(f)


class MorseCoder:
    """Translate between Morse code and text"""

    def __init__(self):
        self.morse_mappings = morse_dict  # for mapping string characters to Morse code
        self.char_mappings = {val: key for key, val in morse_dict.items()}  # for mapping Morse codes to text

    def encode(self, text):
        """Translates text to Morse code"""

        word_list = text.split()
        # create nested list of words, where each word is a list of characters
        nested_chars = [list(word.upper()) for word in word_list]
        # translate each individual character to Morse code
        morse_chars = [[self.morse_mappings[char] for char in word] for word in nested_chars]
        # rejoin characters into words with single spacing as per convention
        morse_words = [" ".join(word) for word in morse_chars]
        # rejoin words into sentence with triple spacing as per convention
        morse_text = "   ".join(morse_words)

        return morse_text

    def decode(self, code):
        """Translates Morse code to plain text"""

        # in Morse code words are separated by triple spaces
        code_list = code.split("   ")
        # create nested list of word-codes, where each word-code is a list of character-codes
        nested_codes = [code.split() for code in code_list]
        # translate each individual character-code to plain text
        text_chars = [[self.char_mappings[char] for char in code] for code in nested_codes]
        # rejoin characters into words
        text_words = ["".join(char) for char in text_chars]
        # rejoin words into sentence with single spacing
        plain_text = " ".join(text_words)

        return plain_text
