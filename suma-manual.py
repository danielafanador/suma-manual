a_list = [4444, 8897, 6340, 9896, 4835, 4324, 10, 6445,
          661, 1246, 1000, 7429, 1376, 8121, 647, 1280,
          3993, 4881, 9500, 6701, 1199, 6251, 4432, 37]

# Este debería ser el resultado - Cálculo automático
print ('Cálculo automático:')
print (sum(a_list))
print (' ')

# Cálculo manual
sum_manual = 0

# Para saber el número de elementos
ext = len(a_list)
print ('Para saber el número de elementos en la lista:')
print (ext)
print (' ')

#Loop - Cálculo manual
for element in a_list:
    sum_manual = element + sum_manual

print ('Resultado calculado manualmente:')
print (sum_manual)
print (' ')
