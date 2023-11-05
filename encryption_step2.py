from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
import os
import encryption_step1

keywords = encryption_step1.encrypted_keywords


# Encrypt a message using AES
# AES encryption algorithm in the Cipher Feedback (CFB) mode.
def encrypt_message(aes_key, plaintext):
    iv = os.urandom(16)  # Generate a random IV (Initialization Vector) of 16 bytes.
    cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv), backend=None)
    encryptor = cipher.encryptor() # creates an encryptor object that will be used to perform the actual encryption.
    ciphertext = encryptor.update(plaintext.encode('utf-8')) + encryptor.finalize()
    return iv + ciphertext

# Decrypt a message using AES
def decrypt_message(aes_key, ciphertext):
    iv = ciphertext[:16]  # Extract the IV from the ciphertext
    ciphertext = ciphertext[16:]  # Remove the IV from the ciphertext
    cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv), backend=None)
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext.decode('utf-8')

# Example message to encrypt
message = ['Hello, Alice! This is a secret message.', 'my name is Ruhan', 'the name of my country is bangladesh']

encrypted_message = []
decrypted_message = []

i=0
for keyword in keywords:
    # Derive an AES key from the shared secret using a KDF (PBKDF2HMAC)
    # Key Derivation Function
    # using PBKDF2HMAC (Password-Based Key Derivation Function 2 with HMAC) is being used to derive an AES encryption key from a shared secret.
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,  # Choose an appropriate number of iterations
        salt=b'salt_value',  # Replace with a secure random salt
        # The salt is a random value used to increase the security of the derived key. 
        length=32,  # Specify the desired key length in bytes. In this case, a 256-bit (32-byte) key is being derived.
        backend=None  # which means the default cryptographic backend will be used.
    )
    # aes_key = kdf.derive(int(shared_secret[0]).to_bytes(32, byteorder='big'))

    # shared_secret_bytes = int(shared_secret_alice[0]).to_bytes(32, byteorder='big')

    symmetric_key = kdf.derive(int(keyword).to_bytes(32, byteorder='big'))
    # aes_key_bob = kdf.derive(int(shared_secret_bob[0]).to_bytes(32, byteorder='big'))


    # Encrypt the message using AES
    encrypted_message.append(encrypt_message(symmetric_key, message[i]))

    # Decrypt the message using AES
    decrypted_message.append(decrypt_message(symmetric_key, encrypted_message[i]))
    i = i+1



# input output
print("\nOriginal Message:", message)
print("\nEncrypted Message:", encrypted_message)
print("\nDecrypted Message:", decrypted_message)


def bytes_to_integer(byte_data):
    # Convert the byte data to an integer
    integer_value = int.from_bytes(byte_data, byteorder='big')
    return integer_value

# Example usage
byte_data = b'\x01\x02\x03\x04'
integer_value = bytes_to_integer(byte_data)
print(integer_value)

def integer_to_bytes(integer_value, byte_length):
    # Convert the integer to byte data with the specified length
    byte_data = integer_value.to_bytes(byte_length, byteorder='big')
    return byte_data

# Example usage
integer_value = 16909060
byte_data = integer_to_bytes(integer_value, 4)  # Specify the desired byte length
print(byte_data)