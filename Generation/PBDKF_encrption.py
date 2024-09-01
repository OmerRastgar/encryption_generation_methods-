import hashlib
import os
import binascii

def generate_key(password, salt=None, iterations=100000, dklen=32):   # Large iteration is required and dklen is 256 bit 
    # Generate a random salt if none is provided
    if salt is None:
        salt = os.urandom(16)
    
    # Derive the key using PBKDF2 with HMAC-SHA256
    key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, iterations, dklen)
    
    # Return the salt and the derived key
    return binascii.hexlify(salt), binascii.hexlify(key)

# Example usage:
password = "your_secure_password"    # would need to secure this password as well. the password not necessarily need a high entropy as hash with salt is used to generate high entropy.
salt, derived_key = generate_key(password)

print(f"Salt: {salt.decode()}")
print(f"Derived Key: {derived_key.decode()}")
