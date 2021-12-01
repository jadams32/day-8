# Welcome to day 8 of the 100 days of code challenge. On this day I build a
# cipher program to encode and decode messages based on Julius Ceasar's encoded
# messages during the roman empire. Play around with the program and encode your
# own messages!

# importing the starting logo art
from logo_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Prints the logo and initalizes a state for the program to loop
print(logo)
program_run = True

# While loop to keep the program running until the user asks not to
while program_run:

# Gather inputs from the user including the text and shift number
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

# Safegaurd for entering a shift number that is too large
    if shift > 26:
        shift = int(input("Shift number cannot be larger than 26 please try again.\nType the shift number:\n"))

# Encryption Function
    def encrypt(text, shift):
        encrypted = []
        for letter in text:
            if letter in alphabet:
                num = alphabet.index(letter) + shift
                encrypted.append(alphabet[num])
            else:
                encrypted.append(letter)

        print(f'The encoded text is {"".join(encrypted)}')

# Decryption Function
    def decrypt(text, shift):
        decrypted = []
        for let in text:
            if let in alphabet:
                num = alphabet.index(let) - shift
                decrypted.append(alphabet[num])
            else:
                decrypted.append(let)
        print(f'The decoded text is {"".join(decrypted)}')

# Logic for choosing wether to encode or decode text
    if direction == "encode":
        encrypt(text, shift)
    else:
        decrypt(text,shift)

# Asking the user if they want to play again.
    play_again = input('Would you like to restart the cipher program? "Yes" or "No"?\n').lower()
    if play_again == "no":
        program_run = False
