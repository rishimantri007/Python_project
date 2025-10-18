from cryptography.fernet import Fernet

def generate_key():
    """Generate a key for encryption."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    """Load the previously generated key."""
    return open("secret.key", "rb").read()

def encrypt_data(data: bytes, key: bytes) -> bytes:
    f = Fernet(key)
    return f.encrypt(data)

def decrypt_data(encrypted_data: bytes, key: bytes) -> bytes:
    f = Fernet(key)
    return f.decrypt(encrypted_data)
