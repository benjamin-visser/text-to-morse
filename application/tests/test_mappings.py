import json
from application import morse_coder


ALPHABET_LIST = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
                 "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                 "S", "T", "U", "V", "W", "X", "Y", "Z"]

NUMERAL_LIST = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

PUNCTUATION_LIST = ["!", "@", "$", "&", "(", ")", "-", "_", "=",
                    "+", "'", ":", ";", ".", ",", "?", "/", "\""]

EXAMPLE_ENCODINGS = [
    (
        "Some text",
        "... ___ __ .   _ . _.._ _"
    ),
    (
        "Once upon a time in Hollywood. Another hit from Tarantino!",
        "___ _. _._. .   .._ .__. ___ _.   ._   _ .. __ .   .. _.   "
        ".... ___ ._.. ._.. _.__ .__ ___ ___ _.. "
        "._._._   ._ _. ___ _ .... . ._.   .... .. _   .._. ._. ___ "
        "__   _ ._ ._. ._ _. _ .. _. ___ _._.__"
    ),
    (
        "@elonmusk is a South African hey...",
        ".__._. . ._.. ___ _. __ .._ ... _._   .. ...   ._   ... ___ "
        ".._ _ ....   ._ .._. ._. .. _._. ._ _.  "
        " .... . _.__ ._._._ ._._._ ._._._"
    ),
    (
        "I'm all bout making that $$$",
        ".. .____. __   ._ ._.. ._..   _... ___ .._ _   __ ._ _._ .. "
        "_. __.   _ .... ._ _   ..._.._ ..._.._ "
        "..._.._"
    ),
    (
        "You could say I'm on call 24/7",
        "_.__ ___ .._   _._. ___ .._ ._.. _..   ... ._ _.__   .. .____."
        " __   ___ _.   _._. ._ ._.. ._..   "
        "..___ ...._ _.._. __..."
    ),
    (
        "2+2-1=3 (That's quick maths)",
        "..___ ._._. ..___ _...._ .____ _..._ ...__   _.__. _ .... ._ _ "
        ".____. ...   __._ .._ .. _._. _._   "
        "__ ._ _ .... ... _.__._"
    ),
    (
        'Shopping list: 1 potato, 9 "onions", 78 python_scripts.',
        "... .... ___ .__. .__. .. _. __.   ._.. .. ... _ ___...   .____"
        "   .__. ___ _ ._ _ ___ __..__   "
        "____.   ._.._. ___ _. .. ___ _. ... ._.._. __..__   __... ___.."
        "   .__. _.__ _ .... ___ _. ..__._ "
        "... _._. ._. .. .__. _ ... ._._._"
    ),
    (
        "easy as xyz, qrs & tuv; or 650!?",
        ". ._ ... _.__   ._ ...   _.._ _.__ __.. __..__   __._ ._. ...   "
        "._...   _ .._ ..._ _._._.   ___ ._. "
        "  _.... ..... _____ _._.__ ..__.."
    )
]

with open("application/morse-dictionary.json", "r") as f:
    morse_dict = json.load(f)


class TestMorseKeys:
    """For testing dictionaries used in translation"""

    def test_alphabet(self):
        """Test that all alphabet characters have a Morse code mapping"""
        for char in ALPHABET_LIST:
            _ = morse_dict[char]

    def test_numerals(self):
        """Test that all numerals have a Morse code mapping"""
        for char in NUMERAL_LIST:
            _ = morse_dict[char]

    def test_punctuation(self):
        """Test that all punctuation marks have a Morse code mapping"""
        for char in PUNCTUATION_LIST:
            _ = morse_dict[char]

    def test_unique(self):
        """Test that each character has a unique Morse code mapping"""
        assert len(set(morse_dict.keys())) == len(set(morse_dict.values()))


class TestCoding:
    """Tests translation accuracy"""

    def test_encoding(self):
        """Test that string is encoded to expected Morse code"""

        for encoding_pair in EXAMPLE_ENCODINGS:
            string, code = encoding_pair
            assert morse_coder.encode(string) == code

    def test_decoding(self):
        """Test that Morse code is decoded to expected string"""

        for encoding_pair in EXAMPLE_ENCODINGS:
            string, code = encoding_pair
            assert morse_coder.decode(code) == string.upper()

    def test_encode_decode(self):
        """Test that encoding and decoding is consistent"""

        for encoding_pair in EXAMPLE_ENCODINGS:
            string, code = encoding_pair

            # Ensures that string encoding is reversible
            encoded_string = morse_coder.encode(string)
            assert morse_coder.decode(encoded_string) == string.upper()

            # Ensures that Morse decoding is reversible
            decoded_code = morse_coder.decode(code)
            assert morse_coder.encode(decoded_code) == code
