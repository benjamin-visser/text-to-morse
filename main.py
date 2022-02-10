from morse_coder import MorseCoder


if __name__ == "__main__":

    coder = MorseCoder()

    while True:
        print("Press any key + enter to quit")
        coding = input("Would you like to encode or decode Morse? (encode/decode): ")

        if coding.lower() == "encode":
            text = input("Write something you'd like to convert to morse code: ").strip()
            print(coder.encode(text))

        elif coding.lower() == "decode":
            text = input("Write some code you'd like to convert to text: ").strip()
            print(coder.decode(text))

        else:
            break
