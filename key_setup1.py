import random
import generator
import hash

# Define a large prime number (for demonstration purposes, you should use a secure prime)
p = generator.p

# Define a generator (for demonstration purposes, you should use a known generator)
g = generator.g1

# Generate a private key (random integer)
xc = random.randint(1, p - 1)

# Compute the public key using modular exponentiation
Dc = pow(g, xc, p)

# Identity information (for demonstration purposes, you can replace this with your IDC)
IDC = "1101010101010101"

Qc = hash.H2(IDC)
# Print the public and private keys
print("Public Key (Dc):", Dc)
print("Private Key (xc):", xc)
print("Dense State Identity (Qc):", Qc)
