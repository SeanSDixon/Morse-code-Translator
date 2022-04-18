MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...',
                    '8':'---..', '9':'----.', '0':'-----',
                    ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-'}

translation = []
sentence = input("What would you like to encode?").upper()
sentence = list(sentence)
try:
    for char in sentence:
        if char == " ":
            pass
        else:
            translation.append(MORSE_CODE_DICT[char])
    print(f"Here is your message: {' '.join(translation)}")

except KeyError:
    print("Sorry, Morsecode does not use one of your characters. Try again :)")

