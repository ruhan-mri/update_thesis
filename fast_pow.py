def fast_exponentiation(base, exponent, modulus=None):
    result = 1
    base = base % modulus if modulus else base  # Apply modulus if given

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus if modulus else result * base
        exponent //= 2
        base = (base * base) % modulus if modulus else base * base

    return result

p = 115792089237316195423570985008687907853269984665640564039457584007908834671663
result = fast_exponentiation(p, p)
print(result)
