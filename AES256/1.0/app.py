#py -m pip install pycryptodome
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def generate_key(password, salt):
    return PBKDF2(password, salt, dkLen=32)

def encrypt_message(password, message):
    salt = get_random_bytes(16)
    key = generate_key(password, salt)

    cipher = AES.new(key, AES.MODE_CBC)

    encrypted = cipher.encrypt(pad(message.encode('utf-8'), AES.block_size))

    with open('encrypted.bin', 'wb') as f:
        f.write(cipher.iv)
        f.write(encrypted)
    return encrypted, key
    

def decrypt_message(key): 
    with open('encrypted.bin', 'rb') as f:
        iv = f.read(16)
        decrypt_data = f.read()
     
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decrypted = unpad(cipher.decrypt(decrypt_data), AES.block_size)
    return decrypted

password = input("password: ")
message = input("message: ")

encriptar, key = encrypt_message(password, message)
print(f"mensaje encriptado: {encriptar}")

desencriptar = decrypt_message(key)
print(f"mensaje desencriptado: {desencriptar}")