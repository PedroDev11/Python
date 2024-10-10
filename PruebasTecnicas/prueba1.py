""" 
En la variable test dispones de una cadena de texto, debes contar las palabras y devolver cuantas veces 
se repiten cada una de ellas.
Ejemplo --> 'nadie' aparece 2 veces
"""

def toLowerCase(text):
    lowerCase = text.lower()
    return lowerCase

def cleanText(textLower):
    cleanedText = textLower.replace(',', '').replace('.', '')
    separedText = cleanedText.split(" ")
    return separedText

def countWords(cleanedText):
    dictionary = {}
    
    for word in cleanedText:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary

text = "Creo que a veces es la gente de la que nadie espera nada, es la que hace cosas que nadie puede imaginar."

lowerCase = toLowerCase(text)
cleanedText = cleanText(lowerCase)
countedWords = countWords(cleanedText)

print(countedWords)
