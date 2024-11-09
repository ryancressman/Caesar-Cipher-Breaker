# Ask the user for the encrypted message
cipher_text = input("Enter the cipher text: ")

# Loop through all 25 possible shifts
for shift in range(1, 26):
    decrypted_message = ""  # Start with an empty string for the decrypted message

    # Go through each character in the cipher text
    for char in cipher_text:
        if char.isalpha():  # If the character is a letter
            # Shift the letter by the current shift value
            # For uppercase letters
            if char.isupper():
                new_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            # For lowercase letters
            else:
                new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            decrypted_message += new_char  # Add the shifted letter to the message
        else:
            decrypted_message += char  # If it's not a letter, just add the character as is

    # Print the result for the current shift
    print(f"Shift {shift}: {decrypted_message}")
