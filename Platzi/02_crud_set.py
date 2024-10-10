set_countries = {'mex', 'col', 'bol'}

size = len(set_countries)
print(size)

print('col' in set_countries)
print('peru' in set_countries)

#add
set_countries.add('peru')
print(set_countries)

#update
set_countries.update({'ar', 'ecu', 'peru'})
print(set_countries)

#remove
#set_countries.remove('ag') manda error si es que ya no encuentra el elemento a remover
set_countries.discard('arg') #Elimina el elemento pero no manda error si es que ya no encuentra ese elemento
print(set_countries)

set_countries.clear()
print(set_countries)
print(len(set_countries))