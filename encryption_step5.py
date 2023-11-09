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
# didn't change anything
