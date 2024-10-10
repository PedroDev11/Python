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
from Crypto.Util.Padding import pad, unpad
import base64

message = {
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

def main():
    # La clave debe tener 16, 24 o 32 bytes para AES-128, AES-192 o AES-256 respectivamente.
    key = b'$3CR3T_p4$$w0rd_'  # 16 bytes para AES-128
    data = str(message)

    # Cifrado
    encrypted_data = encrypt_aes_ecb(key, data)
    print("Texto cifrado:", encrypted_data)

    # Descifrado
    decrypted_data = decrypt_aes_ecb(key, encrypted_data)
    print("\nTexto descifrado:", decrypted_data)

if __name__ == "__main__":
    main()