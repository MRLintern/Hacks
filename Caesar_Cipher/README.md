## Caesar Cipher

### Introduction

Caesar cipher uses keys, which encrypt the message differently
depending on which key is used. The keys for the Caesar cipher are the
integers from 0 to 25 . Even if a cryptanalyst knows the Caesar cipher was
used, that alone doesn’t give them enough information to break the cipher.
They must also know the key.

It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. 
For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.

### Example

* Plain:	A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X	Y	Z
* Cipher:   X	Y	Z	A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W

An example:
  
* Plaintext:  THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
* Ciphertext: QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD

General formulas for encryption/decryption:

Encryption:

     En(x) = (x - n) mod 25

Decryption:

     Dn(x) = (x + n) mod 25,

where in both cases, `x` is the number to be encrypted, and `n` is the value we shift by.

### Requirements

* `pyperclip 1.8.2 `.
* `$ pip install pyperclip`.
* or
* `$ sudo apt-get install xclip` on `Ubuntu`.
* `Python 3.x`.
