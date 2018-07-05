import time,sys
from datetime import datetime
from operator import itemgetter
##VALUE_LIST=('Unix time','Elapsed time','User','Status','Bytes recieved','Request type','URL','USER')

#Valores Iniciales
first=True
users='ftomar.hd,abdcasamayorf,acfleonc'#Lista de usuarios
throughput_list=[]
delay_list=[]
errors=[]
bienvenida='''Este documento contiene información recogida sobre el
experimento QoE/QoS llevada a cabo en la fecha %s.\n\n'''%time.strftime('%d-%m-%Y')

def main(root,users,start_time,end_time):
    users = users.split(',')
    for i in range(len(users)):
        throughput_list.append([])
        delay_list.append([])
        errors.append({})
    st = datetime.strptime(start_time,'%d/%m/%Y %H:%M')
    timestamp1 = st.timestamp()#int(time.mktime(datetuple))
    et = datetime.strptime(end_time,'%d/%m/%Y %H:%M')
    timestamp2 = et.timestamp()#int(time.mktime(datetuple))
    try:
        file=open(root,'r')
    except FileNotFoundError:
        print("The file %s is not located in the current working directory"%root)
        sys.exit(1)
    #Separar linea por elementos
    for line in file:
        if float(line[:15])>=timestamp1 and float(line[:15])<=timestamp2:
            value_list=line.split(' ')
            #Remover espacios en blanco innecesarios
            c=value_list.count('')
            for i in range(c): value_list.remove('')
            #Cálculo del throughput y delay de las peticiones validas por usuario, si es uno de los testados
            if value_list[7]in users :
                status=value_list[3].split('/')
                index=users.index(value_list[7])
                #if not int(status[1])<400 #Aqui solo tomo como errores los codigos mayores de 400
                if int(status[1])>=100 and int(status[1])<400:#Aqui estoy tomando como errores los codigos 000 tambien
                    try:
                        throughput=float(value_list[4])*8/float(value_list[1]) #Cant de (bytes reciv*8 )/elapsed time   
                    except ZeroDivisionError:
                        pass
                    throughput_list[index].append(throughput)
                    delay = float(value_list[1])/1000
                    delay_list[index].append(delay)
##                    if int(value_list[1])>60000:
##                        print(value_list)
                else:
                    create_err_dict(value_list[3],index)
    make_file(users)
    file.close()
    print('Done!!!')
#Crear archivo
def make_file(users):
    '''Método para estructurar el
       archivo del informe'''
    global first
    data=open('data.txt','w')
    for i in users:
        indice=users.index(i)
        avg_throu=prom(throughput_list[indice])
        avg_delay=prom(delay_list[indice])
        dictionary=errors[indice] #dicionario correspondiente a cada usuario
        v=list(dictionary.values())
        error=sum(v)
        if first:   #Mensaje de bienvenida si es la primera vez escribiendo el archivo                    
            first=False
            data.write(' '.center(67,'*')+'\n')
            data.write(bienvenida)
            data.write(' '.center(67,'*')+'\n')
            data.write('Users\t\t\t\tAvg Throughput(b/s)\tAvg Delay(s)\n')
        data.write('\n'+users[indice]+'\t\t\t%0.2f\t\t\t%0.2f\n\nErrors: %d.\n'%(avg_throu,avg_delay,error))
        for key, values in sorted(dictionary.items(),key=itemgetter(1),reverse=True):
            data.write(str(key)+':'+str(values)+'\n')
    data.close()
    return

def prom(data):
    try:
        prom=sum(data)/len(data)
    except ZeroDivisionError:
        prom=0
    return prom

def create_err_dict(status,index):
    '''Aqui agrego el código de error a uno diccionario
    con valor igual número de veces que ha aparecido'''
    dic=errors[index]    #dic es el dicionario correspondiente al usuario en la posicion
    if status in dic:    #index de la lista de usuarios 'users'
        dic[status]+=1
    else:
        dic[status]=1
if __name__=='__main__':
    main('access.log',users,'29/03/2018 8:00','29/03/2018 12:00')
