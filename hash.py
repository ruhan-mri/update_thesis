import hashlib

# Define a large prime 'p' (adjust the value as needed)
p = 115792089237316195423570985008687907853269984665640564039457584007908834671663

def H2(data):
    # Create a hashlib object (you can choose a specific hashing algorithm)
    hash_object = hashlib.sha256()

    # Update the hash with the binary string data
    hash_object.update(data.encode('utf-8'))

    # Calculate the hash digest as an integer
    hash_digest = int(hash_object.hexdigest(), 16) % p

    return hash_digest

def H1(data):
    # Create a hashlib object (you can choose a specific hashing algorithm)
    hash_object = hashlib.sha256()

    # Update the hash with the byte data
    hash_object.update(data)

    # Calculate the hash digest as an integer
    hash_digest = int(hash_object.hexdigest(), 16) % p

    return hash_digest

# Example usage
binary_string = "1101010101010101"
result = H2(binary_string)
# print("Hash result:", result)
