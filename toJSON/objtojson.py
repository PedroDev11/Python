# import required packages
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# custom class
class Student:
    def __init__(self, roll_no, name, batch):
        self.roll_no = roll_no
        self.name = name
        self.batch = batch

def encrypt_aes_ecb(key, data):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_data = pad(data.encode('utf-8'), AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    return base64.b64encode(encrypted_data).decode('utf-8')

def decrypt_aes_ecb(key, encrypted_data):
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_data = base64.b64decode(encrypted_data.encode('utf-8'))
    decrypted_data = cipher.decrypt(encrypted_data)
    return unpad(decrypted_data, AES.block_size).decode('utf-8')
  
# main function
if __name__ == "__main__":
    
    # create two new student objects
    s1 = Student("85", "Swapnil", "IMT")
    s2 = Student("124", "Akash", "IMT")
  
  
    # convert to JSON format
    jsonstr1 = json.dumps(s1.__dict__, indent = 4)
    jsonstr2 = json.dumps(s2.__dict__, indent = 4)
  
    # print created JSON objects
    print(jsonstr1)
    print(jsonstr2)
    
    # La clave debe tener 32 bytes para AES-256.
    k = 'JDNDUjNUX3A0JCR3MHJkXw=='  # 32 bytes para AES-256
    key = base64.b64decode(k.encode('utf-8'))
    
    data = jsonstr1
    
    #Cifrado
    encrypted_data = encrypt_aes_ecb(key, data)
    print("\n\nTexto cifrado:", encrypted_data)

    #encrypted_data = "vYCVAOq/VALgU7BilFS5ZjqJVPIk3n5l8ciBI0DItpA39NooQMyFBD6uo3vtVNXdtOi0iyI27BHpb6HMyHbPiT0NQgegOiekLedWDkKqS96b+b3xz402Jh3F8XiQt3aQO11szMYAV/6bg5Xl/jEe5+RyRuqv3BbY4T6bJr3FonRQ+vdbhdqI08Rr3B9afTL6aCFDqESpWR6a4F4E4pxwgXASCnj0oJIQJG3f6oWbDJKEfZxBAtwaccVdxGB8njzikNoLtq4YZb/WCs+4bLtveSbT1JF22IZnPJNpFkhqonZLDZJfO1lqojmQEL6l9QSfqwWlyChZ0e+iarELDazCpQ=="

    #Descifrado
    decrypted_data = decrypt_aes_ecb(key, encrypted_data)
    print("\n\nTexto descifrado:", decrypted_data)