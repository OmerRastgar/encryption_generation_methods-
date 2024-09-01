from tpm2_pytss import *
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

# Function to get random entropy from TPM
def get_entropy_from_tpm(size):
    # Initialize TPM context
    tcti = TCTIContext('device:/dev/tpmrm0')  # Path to the TPM device (adjust for your system)
    esys_ctx = ESYS_CONTEXT(tcti)

    # Fetch random bytes from TPM's RNG
    random_bytes = esys_ctx.Random(size)
    return random_bytes

# Function to generate cryptographic key using TPM entropy
def generate_key_with_tpm_entropy(key_length=32):
    # Get entropy from TPM
    entropy = get_entropy_from_tpm(key_length)
    print(f"Entropy from TPM: {entropy.hex()}")

    # Using PBKDF2 to derive key from entropy
    salt = b'unique_salt_value'  # In real-world applications, use a securely generated salt
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=key_length,  # Length of the key (in bytes)
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )

    # Derive the key
    key = kdf.derive(entropy)
    print(f"Generated key (AES): {key.hex()}")
    return key

if __name__ == '__main__':
    # Generate a 32-byte key (AES-256 key)
    generate_key_with_tpm_entropy(32)
