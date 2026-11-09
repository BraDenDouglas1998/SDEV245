from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


message = "Secret message for class!"
message_bytes = message.encode()


symmetric_key = Fernet.generate_key()


cipher = Fernet(symmetric_key)


encrypted_message = cipher.encrypt(message_bytes)


decrypted_message = cipher.decrypt(encrypted_message)

print("SYMMETRIC ENCRYPTION")
print("Original:", message)
print("Encrypted:", encrypted_message)
print("Decrypted:", decrypted_message.decode())




private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

encrypted_rsa = public_key.encrypt(
    message_bytes,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)


decrypted_rsa = private_key.decrypt(
    encrypted_rsa,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("\nASYMMETRIC ENCRYPTION")
print("Original:", message)
print("Encrypted:", encrypted_rsa)
print("Decrypted:", decrypted_rsa.decode())