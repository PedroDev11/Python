""" 
Dada una lista de estudiantes y sus calificaciones en un examen, crea un diccionario 
que asocie cada estudiante con su calificación utilizando una comprensión de diccionario.
"""
student_list = [("Daniel", 92), ("Alex", 89), ("Adolf", 90), ("Pedro", 91), ("Ruben", 100)]

comp_dict = {student: cal for student, cal in student_list}
print(comp_dict)