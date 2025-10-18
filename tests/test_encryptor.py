import unittest
from unittest.mock import patch, mock_open
from src.encryptor import generate_key, load_key, encrypt_data, decrypt_data

class TestEncryptor(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open)
    def test_generate_key_creates_file(self, mock_file):
        key = generate_key()
        mock_file.assert_called_once_with("secret.key", "wb")
        self.assertIsInstance(key, bytes)

    def test_encrypt_decrypt_data(self):
        key = generate_key()
        data = b"Hello World"
        encrypted = encrypt_data(data, key)
        decrypted = decrypt_data(encrypted, key)
        self.assertEqual(data, decrypted)

    @patch("builtins.open", new_callable=mock_open, read_data=b'my_key')
    def test_load_key_reads_file(self, mock_file):
        key = load_key()
        mock_file.assert_called_once_with("secret.key", "rb")
        self.assertEqual(key, b'my_key')


if __name__ == "__main__":
    unittest.main()
