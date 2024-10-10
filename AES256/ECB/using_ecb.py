import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import ECB


if __name__ == "__main__":
    # Our message to be kept confidential
    plaintext = b'Fundamental Cryptography in Python'
    print(f"Plaintext: {plaintext}")

    # 256-bit symmetric key
    key = os.urandom(32)

    # AES ECB cipher
    aes_ecb_cipher = Cipher(AES(key), ECB())

    # Encrypt without padding
    ciphertext = aes_ecb_cipher.encryptor().update(plaintext)
    print(f"Ciphertext (no padding): {ciphertext}")

    # Decrypt without padding
    recovered_plaintext = aes_ecb_cipher.decryptor().update(ciphertext)
    print(f"Recovered plaintext (no padding): {recovered_plaintext}")

    # Pad the plaintext
    aes_block_size_in_bits = 128
    pkcs7_padder = padding.PKCS7(aes_block_size_in_bits).padder()
    padded_plaintext = pkcs7_padder.update(plaintext) + pkcs7_padder.finalize()
    print(f"Padded plaintext: {padded_plaintext}")

    # Encrypt with padding
    ciphertext = aes_ecb_cipher.encryptor().update(padded_plaintext)
    print(f"Ciphertext: {ciphertext}")

    # Decrypt with padding
    recovered_plaintext_with_padding = aes_ecb_cipher.decryptor().update(ciphertext)
    print(f"Recovered plaintext + padding: {recovered_plaintext_with_padding}")

    # Remove padding from plaintext
    pkcs7_unpadder = padding.PKCS7(aes_block_size_in_bits).unpadder()
    recovered_plaintext = pkcs7_unpadder.update(recovered_plaintext_with_padding) + pkcs7_unpadder.finalize()
    print(f"Recovered plaintext: {recovered_plaintext}")
    assert (plaintext == recovered_plaintext)