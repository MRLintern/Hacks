"""

The Reverse Cipher

A message is encrypted by printing it in reverse order.

e.g. Hello, Hacker! becomes: !rekcaH ,olleH.

Its not a great cipher because it can be easy to decrypt

You can use this program to reverse the encryption; just enter encrypted text

Instruction:

$ python3 single_string.py
Enter Message to Encrypt/Decrypt:

"""

# message to encrypt/decrypt
message = input('Enter Message to Encrypt/Decrypt: ')

# translated/encrypted message
encrypted_message = ' '

# find the index (position) of the last character of the string
index = len(message) - 1

# look through the entire message, index by index (or character by character) until we finish
while index >= 0:

	encrypted_message += message[index]

	index -= 1

# print out encrypted message
print(encrypted_message)

