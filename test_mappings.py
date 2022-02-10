from morsekeys import morse_dict


alphabet_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                 "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numeral_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

punctuation_list = ["!", "@", "$", "&", "(", ")", "-", "_", "=",
                    "+", "'", ":", ";", ".", ",", "?", "/", "\""]


def test_alphabet():
    for char in alphabet_list:
        print(morse_dict[char])


def test_numerals():
    for char in numeral_list:
        print(morse_dict[char])


def test_punctuation():
    for char in punctuation_list:
        print(morse_dict[char])


def test_unique():
    assert len(set(morse_dict.keys())) == len(set(morse_dict.values()))
