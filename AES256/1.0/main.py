#py -m pip install pycryptodome
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

#Generate a key
simple_key = get_random_bytes(32)
#print(simple_key)

#Generate a salt, this salt is gonna be used for the encryption for the actual key generation
#and the key generation we also need a password 
salt = simple_key
password = "mypassword"

#Generate the actual encryption key, then we´re gonna use the key 
#in a cipher in order to encrypt a message
key = PBKDF2(password, salt, dkLen=32) #the length = 32

#turn this message into a bytes
message = input("Enter a message to encrypt: ")
#Generate a cipher, we gonna use a block cipher, then we gonna cipher de data
cipher = AES.new(key, AES.MODE_CBC)

#We pass the message and the block size
encrypted = cipher.encrypt(pad(message.encode('utf-8'), AES.block_size))

#se crea una archivo .bin con writing bytes ('wb')
with open('encrypted.bin', 'wb') as f:
    f.write(cipher.iv)
    f.write(encrypted)
    
#reading bytes ('rb')
with open('encrypted.bin', 'rb') as f:
    iv = f.read(16)
    decrypt_data = f.read()
    
cipher = AES.new(key, AES.MODE_CBC, iv=iv)
decrypted = unpad(cipher.decrypt(decrypt_data), AES.block_size)


print(f"Origin message: {message}")
print(f"Message encrypted: {encrypted}")
print(f"Message decrypted: {decrypted}")