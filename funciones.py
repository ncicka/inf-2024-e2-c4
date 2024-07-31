## CONJUNTO DE ACCIONES EMPAQUETADAS
def to_list(tupla):
    lista = []
    for x in range(0,len(tupla)):
        lista.append(tupla[x])
    return lista

pasalista= (1,3,5,6,8)

print(pasalista)
print(to_list(pasalista))
