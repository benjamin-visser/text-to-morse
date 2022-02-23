import morse_coder


if __name__ == "__main__":

    while True:
        print("Press any key + enter to quit")
        coding = input("Would you like to encode or decode Morse? "
                       "(encode/decode): ").strip()

        if coding.lower() == "encode":
            text = input("Write something you'd like to convert"
                         " to morse code: ").strip()
            print(morse_coder.encode(text))

        elif coding.lower() == "decode":
            text = input("Write some code you'd like to convert"
                         " to text: ").strip()
            print(morse_coder.decode(text))

        else:
            break
