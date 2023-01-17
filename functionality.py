
MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                   'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                   'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                   '8': '---..', '9': '----.', '0': '-----',
                   ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': ' -.--.-', ' ': '/'}


def convert_message_to_morse_code(input_morse_code_dict, input_message):
    # In morse code, after each letter is translated, there is a space between letters
    # Adding a space at the end of each dict value, so there is space after each letter of the morse code translation
    # When a space is inserted by the user in his/her message, the space gets rendered as a " / "
    for dict_key in input_morse_code_dict:
        input_morse_code_dict[dict_key] += ' '

    morse_message = ''
    for char in input_message:
        if char in MORSE_CODE_DICT:
            converted_char_to_morse = MORSE_CODE_DICT[char]
            morse_message += converted_char_to_morse
    return morse_message


def testing_loop(morse_dict):
    # Message loop in the console
    message_has_finished = False
    while not message_has_finished:
        input_message = input('Write something: ').upper()
        morse_message = convert_message_to_morse_code(morse_dict, input_message)
        print(morse_message)
        if input_message == 'OVER':
            message_has_finished = True

## For testing purposes
# testing_loop(MORSE_CODE_DICT)
