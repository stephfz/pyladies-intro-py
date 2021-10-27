paises_mercosur ={  'Peru': 'Lima',
                     'Chile': 'Santiago',
                     'Argentina' : 'Buenos Aires'   
                }

#recordatorio

##llaves de un diccionario
print(paises_mercosur.keys())

##valores
print(paises_mercosur.values())

 # Imprimir la capital de cada pais
for pais in paises_mercosur.keys():
     print(paises_mercosur[pais])               