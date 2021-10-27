


def promedio_notas(lista_notas):
    acumulado = 0
    for nota in lista_notas:
        acumulado = acumulado + nota
    promedio = acumulado / len(lista_notas)   
    return promedio


notas = [12, 8, 16, 11, 10, 7]

print(promedio_notas(notas))