from Crypto.Cipher import AES
import itertools
import string

# Example ciphertext (in bytes) that you want to decrypt
ciphertext = b'...'  # Replace with your actual ciphertext

# Known plaintext for comparison (for known-plaintext attack)
known_plaintext = b'...'  # Replace with a known part of plaintext

# Function to try a key and check if it decrypts to the known plaintext
def try_key(key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(ciphertext)
    if known_plaintext in decrypted:
        print(f"Key found: {key}")
        return True
    return False

# Brute-force function to try all possible keys (assuming a password-like key)
def brute_force_aes_ecb():
    key_length = 16  # AES-128 (16 bytes key)
    charset = string.ascii_letters + string.digits  # Key characters to try
    for key_candidate in itertools.product(charset, repeat=key_length):
        key = ''.join(key_candidate).encode('utf-8')
        if try_key(key):
            break

# Run the brute force
brute_force_aes_ecb()
