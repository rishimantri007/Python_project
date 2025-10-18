from encryptor import generate_key, load_key, encrypt_data, decrypt_data
from file_manager import read_file, write_file
import os

def main():
    input_file = "/Users/rishi/Desktop/Workspace/Python_project/data/sample.txt"
    encrypted_file = "/Users/rishi/Desktop/Workspace/Python_project/data/sample_encrypted.txt"
    decrypted_file = "/Users/rishi/Desktop/Workspace/Python_project/data/sample_decrypted.txt"

    # Step 1: Generate or load key
    if not os.path.exists("secret.key"):
        key = generate_key()
    else:
        key = load_key()

    # Step 2: Read data
    data = read_file(input_file)

    # Step 3: Encrypt
    encrypted = encrypt_data(data, key)
    write_file(encrypted_file, encrypted)
    print("✅ File encrypted!")

    # Step 4: Decrypt
    decrypted = decrypt_data(encrypted, key)
    write_file(decrypted_file, decrypted)
    print("✅ File decrypted!")

if __name__ == "__main__":
    main()
