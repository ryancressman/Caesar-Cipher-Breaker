# This is a simple Python program to break a Caesar cipher by trying all possible shifts (1-25)
# The program will ask the user to input a cipher text

def caesar_cipher_breaker(cipher_text):
    # Define the alphabet used in the cipher
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Loop through all possible shifts (from 1 to 25)
    for shift in range(1, 26):
        # Create an empty string to store the decrypted message for this shift
        decrypted_text = ''
        
        # Loop through each character in the cipher text
        for char in cipher_text:
            
            # Check if the character is a letter (a-z or A-Z)
            if char.isalpha():
                # Convert the character to lowercase for easy processing
                char_lower = char.lower()

                # Find the index of the character in the alphabet
                index = alphabet.index(char_lower)

                # Calculate the new index by shifting the character backwards
                new_index = (index - shift) % 26  # We use modulo to wrap around if needed

                # Get the new character after the shift
                new_char = alphabet[new_index]

                # If the original character was uppercase, make the decrypted character uppercase
                if char.isupper():
                    decrypted_text += new_char.upper()
                else:
                    # Otherwise, keep the character lowercase
                    decrypted_text += new_char
            else:
                # If the character is not a letter (like spaces or punctuation), leave it unchanged
                decrypted_text += char
        
        # Print the result for this shift
        # The printed text will show all possible shifts, so you can find the right one
        print(f"Shift {shift}: {decrypted_text}")

# Ask the user for the cipher text to break
cipher_text = input("Enter the cipher text you want to break: ")

# Call the function to break the cipher using the user's input
caesar_cipher_breaker(cipher_text)
