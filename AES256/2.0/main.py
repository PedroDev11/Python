from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad
import base64

#Utilizamos el algoritmo PBKDF2 para derivar una clave de la contraseña y la sal
#count: El número de iteraciones que se realizarán durante el proceso de derivación. 
#Cuanto mayor sea este valor, más tiempo llevará el proceso de derivación, 
#lo que aumentará la resistencia a ataques de fuerza bruta.
def generate_key(password, salt):
    return PBKDF2(password, salt, dkLen=32, count=100000)

#Utilizamos el algoritmo AES256, con modo de operacion CBC para encriptar un mensaje
def encrypt(message, password):
    salt = get_random_bytes(16)
    key = generate_key(password, salt)
    
#Se crea un objeto de cifrado AES en modo CBC utilizando la clave generada. El modo CBC es un 
#modo de operación que mejora la seguridad al introducir un vector de inicialización (IV) 
#que se combina con cada bloque de texto claro antes de ser cifrado.
    cipher = AES.new(key, AES.MODE_CBC)
    
#El mensaje proporcionado se codifica en UTF-8 y se rellena (padding) según el tamaño de bloque de AES 
#(que es de 16 bytes). Luego, el mensaje se encripta utilizando el objeto de cifrado AES en modo CBC.
    ciphertext = cipher.encrypt(pad(message.encode('utf-8'), AES.block_size))
    
#Finalmente, el resultado de la encriptación se concatena con la sal y el IV (vector de inicialización)
#utilizado en el proceso de encriptación. Estos valores también se codifican en Base64 
#para asegurarse de que sean representables como cadenas de caracteres. 
#El resultado final es devuelto como una cadena de caracteres codificada en UTF-8.
    return base64.b64encode(salt + cipher.iv + ciphertext).decode('utf-8')


def decrypt(ciphertext, password):
#El texto cifrado se decodifica de Base64 a su representación binaria original utilizando la función
#b64decode
    data = base64.b64decode(ciphertext.encode('utf-8'))
    
#El texto decodificado se divide en tres partes: la sal (salt) de 16 bytes, el vector 
#de inicialización (IV) de 16 bytes y el texto cifrado propiamente dicho. 
#Estos valores se obtienen a partir de la secuencia de bytes decodificada.
    salt, iv, ciphertext = data[:16], data[16:32], data[32:]

#Esta clave se utilizará para desencriptar el texto.
    key = generate_key(password, salt)
    
#Se crea un objeto de cifrado AES en modo CBC utilizando la clave derivada y el IV obtenido del texto 
#cifrado. Esto permite configurar el estado del objeto de cifrado con los parámetros necesarios 
#para desencriptar.
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
#El texto cifrado se desencripta utilizando el objeto de cifrado AES. A continuación, 
#se elimina el relleno (padding) añadido previamente durante el proceso de encriptación 
#El tamaño de bloque de AES (16 bytes) se utiliza como parámetro para el desencriptado.
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

#El texto desencriptado se decodifica de UTF-8 a una cadena de caracteres legible y 
#se devuelve como resultado.
    return plaintext.decode('utf-8')

def main():
    password = input("ingresa una contraseña: ")
    #password = "mysecretkey"  # Cambia esto a tu contraseña secreta
    message = "Hola, este es un mensaje secreto."  # Cambia esto al mensaje que desees

    encrypted_message = encrypt(message, password)
    print("Mensaje encriptado:", encrypted_message)

    password = input("ingresa la contraseña para desencriptar: ")
    decrypted_message = decrypt(encrypted_message, password)
    print("Mensaje desencriptado:", decrypted_message)

if __name__ == "__main__":
    main()
