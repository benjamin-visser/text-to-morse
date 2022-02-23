import json
import numpy as np

# Sample rate in Hz
SAMPLE_RATE = 10000
# 'Dit' duration in seconds
DIT_DURATION = 0.5
# Pitch of output signal in Hz (256Hz corresponds to middle C)
PITCH = 256

with open("morse-dictionary.json", "r") as f:
    encoding_dict = json.load(f)

decoding_dict = {morse_char: plain_char for plain_char, morse_char in
                 encoding_dict.items()}


def encode(text):
    """Translate text to Morse code.

    Arguments:
        text (str): String to convert to Morse code.
            Allowed characters:
            - Alphanumeric (upper or lower case): [A, B, C, D, E, F, G, H, I, J,
                                                   K, L, M, N, O, P, Q, R, S, T,
                                                   U, V, W, X, Y, Z, 0, 1, 2, 3,
                                                   4, 5, 6, 7, 8, 9]
            - Special: ['.', ',', '?', ''', '!', '/', '()', '&', ':', ';', '=',
                        '+', '-', '_', '"', '$', '@']

    Returns:
        morse_code (str): Morse code string containing periods (.), underscores
                          (_), and spaces ( ).
        - e.g. '. _.._ ._ __ .__. ._.. .'
    """

    # create nested list of words, where each word is a list of characters
    word_list = text.split()
    nested_chars = [list(word.upper()) for word in word_list]
    # translate each individual character to Morse code
    morse_chars = [[encoding_dict[char] for char in word] for word in
                   nested_chars]

    # characters are separated by single spaces
    morse_words = [" ".join(word) for word in morse_chars]
    # words are separated by triple spaces
    morse_code = "   ".join(morse_words)

    return morse_code


def decode(morse_code):
    """Translate Morse code to text

    Arguments:
        morse_code (str): Morse code string containing periods (.),
                          underscores (_), and spaces ( ).
        - e.g. '. _.._ ._ __ .__. ._.. .'

    Returns:
        text (str)
    """

    assert len(set('._ ' + morse_code)) == 3, "Input string may only contain" \
                                              "periods (.), " \
                                              "underscores (_), and spaces ( )"

    # in Morse code words are separated by triple spaces
    code_list = morse_code.split("   ")
    # create nested list of words, where each word is a list of character-codes
    nested_codes = [code.split() for code in code_list]
    # translate each individual character-code to text
    text_chars = [[decoding_dict[char] for char in code] for code in
                  nested_codes]
    # rejoin characters into words
    text_words = ["".join(char) for char in text_chars]
    # rejoin words into sentence with single spacing
    text = " ".join(text_words)

    return text


def generate_audio(morse_string):
    """Generate 1D numpy array representing a given Morse signal

    Arguments:
        morse_string (str): Morse code sequence to convert to audio.
                            String can only contain periods (.),
                            underscores (_), and spaces ( ).
        - e.g. '. _.._ ._ __ .__. ._.. .'

    Returns:
        audio_signal (array): 1D array of shape (x,) where x is the length of
                              the generated audio signal. This is
        directly related to the length of the input string.

        SAMPLE_RATE (int): the sample rate used to generate the audio signal.
                           Returned for convenience in writing output
        to .wav file.
    """

    assert len(set('._ ' + morse_string)) == 3, "Input string may only " \
                                                "contain periods (.), " \
                                                "underscores (_), and spaces " \
                                                "( )."

    # Create empty array to append signal snippets to
    audio_signal = np.empty(0)

    # Morse signals are represented by combinations of
    # short and long elements, separated by spaces
    # The short element is often referred to as the 'dit'
    # and is the fundamental time unit of the Morse signal
    dit = np.linspace(0., DIT_DURATION, int(DIT_DURATION * SAMPLE_RATE))
    # The longer element is often referred to as the 'dah'
    # and is three times the duration of the 'dit'
    dah = np.linspace(0., 3 * DIT_DURATION, 3 * int(DIT_DURATION * SAMPLE_RATE))
    # A short spacer is used to make individual 'dits'
    # and 'dahs' discernible in the audio output
    # (this isn't part of the signal)
    element_spacer = np.zeros(int(DIT_DURATION * SAMPLE_RATE / 2))
    # The spaces are equal in duration to the 'dit'
    silence = np.zeros_like(dit)

    amplitude = np.iinfo(np.int16).max

    # create sine waves for 'dits' and 'dahs'
    dit_data = amplitude * np.sin(2. * np.pi * PITCH * dit)
    dah_data = amplitude * np.sin(2. * np.pi * PITCH * dah)

    # fill empty audio_signal array based on input string
    for char in morse_string:
        if char == ".":
            audio_signal = np.concatenate((audio_signal, element_spacer,
                                           dit_data))
        elif char == "_":
            audio_signal = np.concatenate((audio_signal, element_spacer,
                                           dah_data))
        elif char == " ":
            audio_signal = np.concatenate((audio_signal, silence))

    return audio_signal, SAMPLE_RATE
