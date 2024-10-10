# KWARGS

"""def getProduct(**datos):
    print(datos) # {'id': 1, 'name': 'Cheetos', 'descripcion': 'Me gustan mucho los Cheetos'}

getProduct(id=1,
           name="Cheetos",
           descripcion="Me gustan mucho los Cheetos")"""
           
# PALINDROMO
def no_space(text):
    new_text = ""
    for char in text:
        if char != " ":
            new_text += char
    return new_text

def reverse(text):
    text_reverse = ""
    for char in text:
        text_reverse = char + text_reverse
    return text_reverse

def esPalindromo(text: str):
    text = no_space(text)
    text_reverse = reverse(text)
    return text.lower() == text_reverse.lower()

print(esPalindromo("Reconocer"))
print(esPalindromo("Hola mundo"))
print(esPalindromo("Amo la paloma"))