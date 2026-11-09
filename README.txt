README – Python Encryption and Decryption

Project Overview

This project demonstrates two methods of encryption and decryption using Python: symmetric encryption and asymmetric encryption.

The program takes a short message, encrypts it, and then decrypts it back into its original readable form.

Encryption Methods

1. Symmetric Encryption

The program uses Fernet encryption. Symmetric encryption uses the same secret key to encrypt and decrypt a message.

2. Asymmetric Encryption

The program uses RSA encryption. Asymmetric encryption uses two keys:

Public key: Encrypts the message.

Private key: Decrypts the message.

Requirements

Python 3

Cryptography library

Install the required library using:

pip install cryptography

How to Run

Install the cryptography library.

Save the Python code in a file named encryption.py.

Open a terminal or command prompt.

Run the program using:

python encryption.py

Expected Results

The program displays:

The original message.

The encrypted message.

The decrypted message.

Both encryption methods should successfully decrypt the message and display the original text.

Conclusion

This project demonstrates how symmetric and asymmetric encryption work. It shows how encryption protects information and how decryption makes that information readable again.