import numpy as np
from scipy.io.wavfile import write

SAMPLE_RATE = 10000
DIT_DURATION = 0.5
PITCH = 256


def audio_generator(morse_string):

    audio_signal = np.empty(0)

    dit = np.linspace(0., DIT_DURATION, int(DIT_DURATION * SAMPLE_RATE))
    dah = np.linspace(0., 3 * DIT_DURATION, 3 * int(DIT_DURATION * SAMPLE_RATE))
    spacer = np.zeros(int(DIT_DURATION * SAMPLE_RATE / 2))
    silence = np.zeros_like(dit)

    amplitude = np.iinfo(np.int16).max

    dit_data = amplitude * np.sin(2. * np.pi * PITCH * dit)
    dah_data = amplitude * np.sin(2. * np.pi * PITCH * dah)

    for char in morse_string:
        if char == ".":
            audio_signal = np.concatenate((audio_signal, spacer, dit_data))
        elif char == "_":
            audio_signal = np.concatenate((audio_signal, spacer, dah_data))
        elif char == " ":
            audio_signal = np.concatenate((audio_signal, silence))

    write("example.wav", SAMPLE_RATE, audio_signal.astype(np.int16))
