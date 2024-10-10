"""
$3CR3T_p4$$w0rd_

{
    "arrayColores":[{
            "nombreColor":"rojo",
            "valorHexadec":"#f00"
        },
        {
            "nombreColor":"verde",
            "valorHexadec":"#0f0"
        },
        {
            "nombreColor":"azul",
            "valorHexadec":"#00f"
        },
        {
            "nombreColor":"cyan",
            "valorHexadec":"#0ff"
        },
        {
            "nombreColor":"magenta",
            "valorHexadec":"#f0f"
        },
        {
            "nombreColor":"amarillo",
            "valorHexadec":"#ff0"
        },
        {
            "nombreColor":"negro",
            "valorHexadec":"#000"
        }
    ]
}
"""
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

data = {
    "arrayColores":[{
            "nombreColor":"rojo",
            "valorHexadec":"#f00"
        },
        {
            "nombreColor":"verde",
            "valorHexadec":"#0f0"
        },
        {
            "nombreColor":"azul",
            "valorHexadec":"#00f"
        },
        {
            "nombreColor":"cyan",
            "valorHexadec":"#0ff"
        },
        {
            "nombreColor":"magenta",
            "valorHexadec":"#f0f"
        },
        {
            "nombreColor":"amarillo",
            "valorHexadec":"#ff0"
        },
        {
            "nombreColor":"negro",
            "valorHexadec":"#000"
        }
    ]
}

#Ten en cuenta que el tamaño del mensaje debe ser múltiplo de 16 bytes (tamaño del bloque AES). 
#Si el mensaje no es múltiplo de 16 bytes, se agregará un padding para que tenga una longitud 
#válida antes de encriptar.

def pad(text):
    # Completa el texto para que sea múltiplo de 16 bytes (tamaño de bloque AES)
    while len(text) % 16 != 0:
        text += b' '
    return text


def encrypt_AES_ECB(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted = cipher.encrypt(pad(plaintext))
    return base64.b64encode(encrypted)

def decrypt_AES_ECB(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(base64.b64decode(ciphertext))
    return decrypted.rstrip(b' ')  # Elimina el padding al desencriptar

def main():
    #key = get_random_bytes(16)  # Clave de 16 bytes para AES-128

    key = b"$3CR3T_p4$$w0rd_"
    
    # Mensaje a encriptar
    message = b""

    # Encriptar
    encrypted_message = encrypt_AES_ECB(key, message)
    print("Mensaje encriptado:", encrypted_message.decode())

    # Desencriptar
    decrypted_message = decrypt_AES_ECB(key, encrypted_message)
    print("Mensaje desencriptado:", decrypted_message.decode())

if __name__ == "__main__":
    main()
