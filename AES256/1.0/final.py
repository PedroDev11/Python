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

    iv = cipher.iv
    
    return encrypted, key, iv
    

def decrypt_message(key, decrypt_data, iv): 
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decrypted = unpad(cipher.decrypt(decrypt_data), AES.block_size)
    return decrypted

"""
password = input("password: ")
message = input("message: ")

encriptar, key, iv = encrypt_message(password, message)
print(f"mensaje encriptado: {encriptar}")
print(f"key: {key}")
"""

key = b'z?\xe1IJ\x83\xc1\xd4;\xef\x1d\x02\x1c\xc1\xb2\xb4\xfe\x1f\xb0\x94|\x12B\xb6\xbeO\x82\x9fr\r2%'
encriptar = b'"\xce\x9f\x86\xf7!b\xdc+*X7\xeae2\xc8'
iv = b'\xb4\ryQ\xbb\xb1\xbb\xde\x9b3y\x17\xbeO\x06\xb5'

desencriptar = decrypt_message(key, encriptar, iv)
print(f"mensaje desencriptado: {desencriptar}")