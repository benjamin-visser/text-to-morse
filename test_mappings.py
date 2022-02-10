from morsekeys import morse_dict
from morse_coder import MorseCoder

alphabet_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                 "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numeral_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

punctuation_list = ["!", "@", "$", "&", "(", ")", "-", "_", "=",
                    "+", "'", ":", ";", ".", ",", "?", "/", "\""]

morse_strings = ["... ___ __ .   _ . _.._ _",
                 "___ _. _._. .   .._ .__. ___ _.   ._   _ .. __ .   .. _.   .... ___ ._.. ._.. _.__ .__ ___ ___ _.. "
                 "._._._   ._ _. ___ _ .... . ._.   .... .. _   .._. ._. ___ __   _ ._ ._. ._ _. _ .. _. ___ _._.__",
                 ".__._. . ._.. ___ _. __ .._ ... _._   .. ...   ._   ... ___ .._ _ ....   ._ .._. ._. .. _._. ._ _.  "
                 " .... . _.__ ._._._ ._._._ ._._._",
                 ".. .____. __   ._ ._.. ._..   _... ___ .._ _   __ ._ _._ .. _. __.   _ .... ._ _   ..._.._ ..._.._ "
                 "..._.._",
                 "_.__ ___ .._   _._. ___ .._ ._.. _..   ... ._ _.__   .. .____. __   ___ _.   _._. ._ ._.. ._..   "
                 "..___ ...._ _.._. __...",
                 "..___ ._._. ..___ _...._ .____ _..._ ...__   _.__. _ .... ._ _ .____. ...   __._ .._ .. _._. _._   "
                 "__ ._ _ .... ... _.__._",
                 "... .... ___ .__. .__. .. _. __.   ._.. .. ... _ ___...   .____   .__. ___ _ ._ _ ___ __..__   "
                 "____.   ._.._. ___ _. .. ___ _. ... ._.._. __..__   __... ___..   .__. _.__ _ .... ___ _. ..__._ "
                 "... _._. ._. .. .__. _ ... ._._._",
                 ". ._ ... _.__   ._ ...   _.._ _.__ __.. __..__   __._ ._. ...   ._...   _ .._ ..._ _._._.   ___ ._. "
                 "  _.... ..... _____ _._.__ ..__.."]

plain_text_strings = ["Some text",
                      "Once upon a time in Hollywood. Another hit from Tarantino!",
                      "@elonmusk is a South African hey...",
                      "I'm all bout making that $$$",
                      "You could say I'm on call 24/7",
                      "2+2-1=3 (That's quick maths)",
                      'Shopping list: 1 potato, 9 "onions", 78 python_scripts.',
                      "easy as xyz, qrs & tuv; or 650!?"]


class TestMorseKeys:

    def test_alphabet(self):
        for char in alphabet_list:
            print(morse_dict[char])

    def test_numerals(self):
        for char in numeral_list:
            print(morse_dict[char])

    def test_punctuation(self):
        for char in punctuation_list:
            print(morse_dict[char])

    def test_unique(self):
        assert len(set(morse_dict.keys())) == len(set(morse_dict.values()))


class TestCoding:

    def test_encoding(self):
        """Test that string is encoded to expected Morse code"""

        coder = MorseCoder()

        for string, code in zip(plain_text_strings, morse_strings):
            assert coder.encode(string) == code

    def test_decoding(self):
        """Test that Morse code is decoded to expected string"""

        coder = MorseCoder()

        for string, code in zip(plain_text_strings, morse_strings):
            assert coder.decode(code) == string.upper()

    def test_encode_decode(self):
        """Test that encoding and decoding is consistent"""

        coder = MorseCoder()

        for string, code in zip(plain_text_strings, morse_strings):

            # Ensures that string encoding is reversible
            encoded_string = coder.encode(string)
            assert coder.decode(encoded_string) == string.upper()

            # Ensures that Morse decoding is reversible
            decoded_code = coder.decode(code)
            assert coder.encode(decoded_code) == code
