from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

# HKDF is designed to securely derive multiple cryptographic keys from an initial high-entropy key 
# or a "master key" (often called the input key material, or IKM). The IKM is assumed to already
# be a strong key, unlike PBKDF2 which deals with passwords.


def derive_key_from_hkdf(input_key_material, salt=None, info=b'', length=32):
    hkdf = HKDF(
        algorithm=hashes.SHA256(),
        length=length,
        salt=salt,
        info=info,
        backend=default_backend()
    )
    derived_key = hkdf.derive(input_key_material)
    return derived_key

# Example usage:
ikm = b'your_master_key_material'  # High-entropy key (not a password)
salt = b'random_salt_value'        # Optional salt
derived_key = derive_key_from_hkdf(ikm, salt)

print(f"Derived Key: {derived_key.hex()}")
