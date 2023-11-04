import random
import hash
import generator
import encryption_step2

p = generator.p
g1  = generator.g1
# Generate a random private key "a" from Zp*
a = random.randint(1, p - 1)

# Compute the public key PKA
PKA = pow(g1, a, p)

# List of file identifiers (FID0j) and file contents (C0j)
file_identifiers = ["file1", "file2", "file3"]
file_contents = encryption_step2.encrypted_message

# Generate encrypted signature collection for each file
encrypted_signatures = []
i = 0
for file_identifier in file_identifiers:
    H2_result = hash.H2(file_identifier)
    H1_result = hash.H1(file_contents[i])
    
    step1 = pow(g1, H2_result, p)
    step2 = ((H1_result % p) * (step1 % p)) % p
    signature = pow(step2,a,p)
    
    encrypted_signatures.append(signature)
    i = i + 1

# Print the generated public key and encrypted signature collection
print("Public Key PKA:", PKA)
print("Encrypted Signature Collection:")
for i, signature in enumerate(encrypted_signatures):
    print(f"File {i + 1}: {signature}")
