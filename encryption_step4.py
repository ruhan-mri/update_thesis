import random
import generator
import key_setup2

p = generator.p
g1  = generator.g1

# Generate a random private key "s,r" from Zp*
s = random.randint(1, p - 1)
r = random.randint(1, p - 1)

Is = pow(g1, s, p)
I_dash = pow(key_setup2.Du, -r, p)
Io = pow(g1, r, p)

