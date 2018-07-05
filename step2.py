import json


def step2_load(table_name):
    with open('{}.json'.format(table_name)) as f:
        dic = json.load(f)
        lista = []
        for fila in sorted(dic.keys()):  ####ordenar las filas al ingresarlas a la lista
            lista.append(dic[fila])
    return lista#####retornarle diccionario con todas las tablas,llave-nombre da tabla,valor-lista con filas

def step2_write(table_name,lista):###nos devuelve nombre da tabla y lista con filas
    dic = {}
    for num,fila in enumerate(lista):
        dic[num+1] = fila
    with open('{}.json'.format(table_name),'w') as f:
        json.dump(dic,f)

