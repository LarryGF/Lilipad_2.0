import json,os,datetime
import zabixmaster as zb
import opennebula 
from readingdbmodif import percentil,rank,mean

def load(table_name):
    for root,dirs,files in os.walk(os.getcwd()):
        for file in files:
            if file == str(table_name)+'.json':
                path = os.join(root,file)
                with open(path) as f:
                    dic = json.load(f)
                    lista=[]
                for fila in sorted(dic.keys()):  
                    lista.append(dic[fila])
                return lista 

            # except FileNotFoundError:
            #     dic={}
            #     with open('{}.json'.format(table_name),'w') as f:
            #         json.dump(dic,f)

def write(table_name,lista):###nos devuelve nombre da tabla y lista con filas
    with root,dirs,files in os.walk(os.getcwd()):
        for file in files:
            if file == str(table_name)+'.json':
                path = os.join(root,file)
                break
    dic = {}
    for num,fila in enumerate(lista):
        dic[num+1]=fila
    with open(path,'w') as f:
        json.dump(dic,f)


    



