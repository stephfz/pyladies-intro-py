about_me ={
    'nombre' : 'Stephanie',
    'apellido_paterno' : 'Frias',
    'appellido_materno' : 'Zamalloa',
    'edad' : 37
}

for k in about_me.keys():
    print('{} : {}'.format(k , about_me[k]))

#agregar color favorito
about_me['color_favorito'] = 'morado'

for k in about_me.keys():
    print('{} : {}'.format(k , about_me[k]))