import eel
import json
from step_1 import step_1,step_1_load
# from step2 import step2_write,step2_load
from step_4 import *
from step_5 import *
from step_6 import *



eel.init('web')

def write(table,lista):
    print(table,lista)
    dic = {}
    for num,fila in enumerate(lista):
        dic[num+1] = fila
    with open('{}.json'.format(table),'w') as f:
        json.dump(dic,f)

def load_list(table):
    print(table)
    with open('{}.json'.format(table)) as f:
        dic = json.load(f)
        lista = []
        for fila in sorted(dic.keys()):  ####ordenar las filas al ingresarlas a la lista
            lista.append(dic[fila])
    print(lista)
    return lista

@eel.expose
def handler(step,table,dictio):
    print(step)
    print(table)
    print(dictio)
    if step == 1:
        step_1(dictio)
    elif step == 5:
        step5(dictio['service'],dictio['user'],dictio['password'],dictio['ip'],dictio['start_time'],dictio['end_time'])
    else:
        write(table,dictio)

    
@eel.expose
def load(step,table_list):
    if step == 1:
        values = step_1_load()
        return values


    else:
        print(step,table_list)
        result = load_list(table_list)
        return result
@eel.expose
def tests(dictionary):	
    try:
        var=step_4(dictionary) 
    except Exception as e:
        print(e)
        return 'Error'
    return var

eel.start('lilipad1.html')
