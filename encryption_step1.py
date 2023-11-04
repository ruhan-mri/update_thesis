import hash
import key_setup2

# Define a secret value (σ) - you can generate a random value for better security
secret_value = str(key_setup2.shared_secret)

# Set of keywords (W)
keywords = ["apple", "banana", "cherry"]

# Initialize an empty list for encrypted keywords (W')
encrypted_keywords = []

# Encrypt each keyword and add it to the encrypted_keywords list (W')
for keyword in keywords:
    concatenated_value = secret_value + keyword
    encrypted_keyword = hash.H2(concatenated_value)
    encrypted_keywords.append(encrypted_keyword)

# Print the original keywords and their encrypted versions
print("Original Keywords (W):", keywords)
print("Encrypted Keywords (W'):", encrypted_keywords)