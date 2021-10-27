


def es_palindrome(palabra):
  lista_carateres = list(palabra)
  lista_revertida =[]
  for c in range(0 , len(palabra)):
    lista_revertida.append(lista_carateres.pop())
  palabra_revertida =''
  palabra_revertida = palabra_revertida.join(lista_revertida)
  return (palabra_revertida == palabra)


palabra = 'arenera'
print(es_palindrome(palabra))
