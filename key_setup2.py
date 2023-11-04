import hashlib
import random
import generator
import hash

# Define prime numbers p and q (for demonstration purposes)
p = generator.p  # A 10-digit prime number

# Define a generator g1 (for demonstration purposes)
g1 = generator.g1


# Diffie-Hellman Key Exchange
def diffie_hellman_key_exchange(xA, Du, p):
    # Compute shared secret key σ
    sigma = pow(Du, xA, p)
    return sigma

# Example usage:


# Generate a private key xu from Zq*
xu = random.randint(1, p - 1)

# Compute public key Du
Du = pow(g1, xu, p)

# User (DU) key generation
user_identity = "101010"
Qu = hash.H2(user_identity)

# Server (DO) key generation
xA = random.randint(1, p - 1)
PA = pow(g1, xA, p)

# Diffie-Hellman key exchange
shared_secret = pow(Du, xA, p)

# Print the public and private keys
print("Public Key (Du):", Du)
print("Private Key (xa):", xA)
print("Dense State Identity (Qu):", Qu)
print("Shared Secret sigma:", shared_secret)
