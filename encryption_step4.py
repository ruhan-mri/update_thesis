import random
import generator
import key_setup1
import key_setup2
import encryption_step1
import encryption_step2
from integer_pairing import cantor, szudzik
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes



p = generator.p
g1  = generator.g1
keywords = encryption_step1.encrypted_keywords

# Generate a random private key "s,r" from Zp*
s = random.randint(1, p - 1)
r = random.randint(1, p - 1)

Is = pow(g1, s, p)
I_dash = pow(key_setup2.Du, -r, p)
Io = pow(g1, r, p)

# cantor.pair(11, 13) # 313
# cantor.unpair(313) # (11, 13)
beta = cantor.pair(key_setup1.Dc, key_setup1.Qc)
beta = pow(beta, -s, p)
beta = (r * beta) % p

Ii = []
for keyword in keywords:
    temp = (key_setup2.Du * pow(g1, keyword, p)) % p
    Ii.append(pow(temp, beta , p))

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    iterations=100000,  # Choose an appropriate number of iterations
    salt=b'salt_value',  # Replace with a secure random salt
    # The salt is a random value used to increase the security of the derived key. 
    length=32,  # Specify the desired key length in bytes. In this case, a 256-bit (32-byte) key is being derived.
    backend=None  # which means the default cryptographic backend will be used.
)

key = kdf.derive(int(key_setup2.shared_secret).to_bytes(32, byteorder='big'))
I_bar = encryption_step2.encrypt_message(key , beta)
print(I_bar)
