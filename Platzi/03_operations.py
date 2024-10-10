set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

#union con .union y también con el símbolo '|'
set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b)

#intersección
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)

#diferencia, deja los emenetos del conjunto 1 removiendole los del segundo (es una resta, quitamos los elementos de b en a)
set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)

#diferencia simetrica, hace la union del conjunto sin elementos duplicados
set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)