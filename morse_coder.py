from morsekeys import morse_dict


class MorseCoder:

    def encode(self, text):

        word_list = text.split()
        nested_chars = [list(word.upper()) for word in word_list]
        morse_chars = [[morse_dict[char] for char in word] for word in nested_chars]
        morse_words = [" ".join(word) for word in morse_chars]
        morse_text = "   ".join(morse_words)

        return morse_text

    def decode(self, code):

        morse_dict_ivd = {val: key for key, val in morse_dict.items()}
        code_list = code.split("   ")
        nested_codes = [code.split() for code in code_list]
        text_chars = [[morse_dict_ivd[char] for char in code] for code in nested_codes]
        text_words = ["".join(char) for char in text_chars]
        plain_text = " ".join(text_words)

        return plain_text
