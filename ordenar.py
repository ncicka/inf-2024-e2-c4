## ORDENAR LISTAS

# insercion
def insercion(lista):
    nro_elem = len(lista)
    for x in range(1,nro_elem):
        key = lista[x]
        print('key',key)
        j = x - 1
        while j >= 0 and lista[j] > key:
            lista[j+1] = lista[j]
            j =  j - 1
        lista[j+1] = key
            
    return lista

# burbuja
def intercambio(lista):
    nro_elem = len(lista) -1
    for x in range(0,nro_elem):
        for j in range(0,nro_elem):
            if lista[j] > lista[j+1]:
                inter = lista[j]
                lista[j]=lista[j+1]
                lista[j+1] = inter
    return lista

# seleccion
def seleccion(lista):
    for x in range(len(lista)):
        min_i = x
        for j in range(x + 1, len(lista)):
            if lista[j] < lista[min_i]:
                min_i = j
        lista[x], lista[min_i] = lista[min_i], lista[x]
    return lista


ordenar= [70,60,80,0,90,85]
ordenar1= [70,60,80,0,90,85]
ordenar2= [70,60,80,0,90,85]

print(intercambio(ordenar))
print(insercion(ordenar1))
print(seleccion(ordenar2))