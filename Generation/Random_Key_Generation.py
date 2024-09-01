import secrets

# System CSPRNGs like CryptGenRandom or BCryptGenRandom gather entropy from various sources 
# within the system. This is secure and sufficient for many applications. However, in some cases, 
# a key derived from specific sources of entropy (e.g., from hardware-based entropy like a Trusted 
# Platform Module (TPM) or from external cryptographic devices) may be preferred or required.


def generate_secure_key(length=32):
    # Generate a secure random key of the specified length in bytes
    key = secrets.token_bytes(length)   # uses Win 32 api specifically Windows Cryptography API (CAPI) which is (FIPS) 140 certified. 
    return key

# Example usage:
secure_key = generate_secure_key(32)  # Generate a 256-bit key (32 bytes)
print(f"Secure Random Key (hex): {secure_key.hex()}")