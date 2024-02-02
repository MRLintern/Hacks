"""

Program for the Caesar Cipher

See the README for more information on how this cipher works

"""

import pyperclip

# string to be encrypted
message = 'My name is Julius Caesar, and my Credit Card Number is: 2345 2322 2222 8787'

# encryption/decryption key: n; refer to the README file r.e. information on n
key = 13

# mode for encryption/decryption
mode = 'encrypt' # replace with 'decrypt' for decryption

# need symbols that can be encrypted
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789 !?#.'

# variable to store the encrypted/decrypted message
translated_message = ''

for symbol in message:

	if symbol in SYMBOLS:


		# find the index in the SYMBOLS string where symbol is
		symbolIndex = SYMBOLS.find(symbol)

		# -- Perform encryption/decryption

		if mode == 'encrypt': # En(x) = (x + n) mod 26

			translatedIndex = symbolIndex + key

		elif mode == 'decrypt': # Dn(x) = (x - n) mod 26

			translatedIndex = symbolIndex - key

		"""

		CAUTION: 

		len(SYMBOLS) = 66

		1. If the encrypted-letter index is larger than whats available out of all the symbols,

		we need to subtract to get to the correct index of the encrypted letter.

		2. If we are decrypting a message, we add the length of the symbols to the encrypted-letter index.


		"""
		
		# encrypted symbol index is greater than 66
		if translatedIndex >= len(SYMBOLS):

			translatedIndex = translatedIndex - len(SYMBOLS) # correct encrypted symbol index

		
		elif translatedIndex < 0:

			translatedIndex = translatedIndex + len(SYMBOLS)


		translated_message = translated_message + SYMBOLS[translatedIndex] # add encrypted/decrypted symbol to translated (encrypted/decrypted) string

	else:

		# a symbol wasn't found in SYMBOLS so it won't be encrypted/decrypted; add the symbol to the end of the translated (encrypted/decrypted) string
		translated_message = translated_message + symbol

# output result
print(translated_message)

# copy the encrypted/decrypted string to the clipboard
pyperclip.copy(translated_message)
