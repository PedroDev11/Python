my_string = "pepe"
my_other_string = 'rojas'

print(my_string, my_other_string)
print(my_string + " " + my_other_string)

my_line = "Esto es un string\ncon salto de línea"
print(my_line)
my_second_line = "\tEsto es un string con tabulación"
print(my_second_line)

#Formateo
name, secondname, age = "pedro", "alberto", 21
#para trabajar directamente con el objeto, trallendo datos
print("mi nombre es {} {} y mi edad es {}".format(name, secondname, age))

#para trabajar con el numero formateado, cadena de texto y cadenas numericas
print("mi nombre es %s %s y mi edad es %d " %(name, secondname, age))

#inferencia de datos
print(f"mi nombre es {name} {secondname} y mi edad es {age}")

#Desempaquetado de caracteres
language = "python"
a, b, c, d, e, f = language

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(a, b, c, d, e, f)
print(a + b + c + d + e + f)

#División
language_slice = language[1:4]
print(language_slice)

language_slice = language[0:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

#Reverse
reversed_language = language[::-1]
print(reversed_language)

#métodos o funciones del sistema
print(language.capitalize())
print(language.upper())
print(language.count("y"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper()) #evaluar si todas son mayusculas
print(language.startswith("th"))