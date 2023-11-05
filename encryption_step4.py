import random
import generator
import key_setup1
import key_setup2
import encryption_step1
import encryption_step2
from integer_pairing import cantor, szudzik


p = generator.p
g1  = generator.g1

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
Ii = (key_setup2.Du * pow(g1, encryption_step1.encrypted_keywords[0], p)) % p
Ii = pow(Ii, beta , p)

# I_bar = encryption_step2.encrypt_message(beta)
print(Ii)
