from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf import scrypt
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

# By default, ECDH does not change its keys periodically on its own.
# The private and public keys used in the exchange are typically static 
# until they are explicitly regenerated or rotated by the application or system.


# Party 1 computes the shared secret using 𝑃1_priv   and 𝑃2_pub 
# Party 2 computes the shared secret using 𝑃2_priv  and 𝑃1_pub 


# Generate keys for Party 1
private_key_party1 = ec.generate_private_key(ec.SECP256R1(), default_backend())
public_key_party1 = private_key_party1.public_key()

# Serialize public key to share with Party 2
public_key_pem_party1 = public_key_party1.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Generate keys for Party 2
private_key_party2 = ec.generate_private_key(ec.SECP256R1(), default_backend())
public_key_party2 = private_key_party2.public_key()

# Serialize public key to share with Party 1
public_key_pem_party2 = public_key_party2.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Party 1 receives public key from Party 2 and generates shared secret
public_key_party2_loaded = serialization.load_pem_public_key(public_key_pem_party2, backend=default_backend())
shared_secret_party1 = private_key_party1.exchange(ec.ECDH(), public_key_party2_loaded)

# Party 2 receives public key from Party 1 and generates shared secret
public_key_party1_loaded = serialization.load_pem_public_key(public_key_pem_party1, backend=default_backend())
shared_secret_party2 = private_key_party2.exchange(ec.ECDH(), public_key_party1_loaded)

# Both parties should have the same shared secret
assert shared_secret_party1 == shared_secret_party2

# Derive a key from the shared secret (optional)
kdf = scrypt.Scrypt(
    length=32,
    salt=b'some_salt',
    n=2**14,
    r=8,
    p=1,
    backend=default_backend()
)
key = kdf.derive(shared_secret_party1)

print(f"Shared secret: {shared_secret_party1.hex()}")
print(f"Derived key: {key.hex()}")
