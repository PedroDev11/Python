#py -m pip install PyCryptodome
from Crypto.Cipher import AES
from secrets import token_bytes

#token de 16 bytes
key = token_bytes(16)

def encrypt(message):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    cipher_text, tag = cipher.encrypt_and_digest(message.encode('utf-8'))
    return nonce, cipher_text, tag
    
def decrypt(noce, cipher_text, tag):
    cipher = AES.new(key, AES.MODE_EAX, nonce=noce)
    plain_text = cipher.decrypt(cipher_text)
    
    try:
        cipher.verify(tag)
        return plain_text.decode('utf-8')
    except:
        return False

message = input("Enter a message to encrypt: ")

nonce, cipher_text, tag = encrypt(message)

plain_text = decrypt(nonce, cipher_text, tag)

print(f"Cipher text: {cipher_text}")

if not plain_text:
    print("Error to decrypt the message")
else:
    print(f"Plain text: {plain_text}")