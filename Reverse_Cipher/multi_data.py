"""

The reverse cipher.

Program accepts a txt file of credit card details, or some other secure data.

The file of data is read, reversed and printed to a new file.

Not the best cipher as its decrypt.

"""


# Open the file in write mode
encrypted_cc_details = open("cc_details_encrypted.txt", "w")
 

with open("cc_details_uncrypted.txt", "r") as uncrypted_cc_details:

    uncrypted_cc_data = uncrypted_cc_details.read()
 

encrypted_cc_data = uncrypted_cc_data[::-1]
 

encrypted_cc_details.write(encrypted_cc_data)
 
encrypted_cc_details.close()

