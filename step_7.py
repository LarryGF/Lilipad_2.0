import json
import os

 
def step7(servicio):
    utilizacion_fut = {}
    utilizacion_inm = {}
    row = {}
    dic_to_save = {}
    util_inm_cpu = 0
    util_fut_cpu = 0
    '''Formula:
    Utilizaciónfutura=Utilizaciónactual*Usuariosfuturos/Usuariosactuales*β
    '''
    with open('{}.json'.format(os.path.join(os.getcwd(),'step6',servicio))) as f:
        utilizacion = json.load(f)
    with open('step_1.json') as f:
        user_dic = json.load(f)
        print(user_dic)

    users_act = user_dic['usract']
    users_new  = user_dic['usrnew']
    users_fut = user_dic['usrfutr']

    for root,dirnames,files in os.walk(os.path.join(os.getcwd(),'step5',servicio)):
        for file in files:
            with open(os.path.join(root,file)) as f:
                vm = json.load(f)
            pmax = vm['Index']['CPU Usage']['Percentil_max']
            pmax_calc_inm = round(float(pmax)*float(users_new)/float(users_act),2)
            util_inm_cpu += int(pmax_calc_inm/100)+1
            pmax_calc_fut = round(float(pmax)*float(users_fut)/float(users_act),2)
            util_fut_cpu += int(pmax_calc_fut/100)+1
    
    for item in utilizacion.keys():
        util_act = utilizacion[item]['Percentil_max']
        if item == 'CPU Usage':
            utilizacion_fut[item]=util_fut_cpu
            utilizacion_inm[item]=util_inm_cpu
        else:
            util_fut = round(float(util_act)*float(users_fut)/float(users_act),2)
            util_inm = round(float(util_act)*float(users_new)/float(users_act),2)
            utilizacion_fut[item] = util_fut
            utilizacion_inm[item] = util_inm
        
    row['service'] = servicio

    for key in utilizacion_fut:
        if key == 'read.sda':
            row['read'] = utilizacion_fut[key]

        elif key == 'Incoming network traffic on $1':
            row['in'] = utilizacion_fut[key]

        elif key == 'Used disk space on $1':
            row['disk_usage'] = utilizacion_fut[key]

        elif key == 'RAM-used':
            row['ram'] = utilizacion_fut[key]

        elif key == 'Outgoing network traffic on $1':
            row['out'] = utilizacion_fut[key]

        elif key == 'CPU Usage':
            row['cpu'] = utilizacion_fut[key]

        elif key == 'write.sda':
            row['write'] = utilizacion_fut[key]

        elif key == 'iostat.sda':
            row['iops'] = utilizacion_fut[key]



    for key in utilizacion_inm:
        if key == 'read.sda':
            row['read2'] = utilizacion_inm[key]

        elif key == 'Incoming network traffic on $1':
            row['in2'] = utilizacion_inm[key]

        elif key == 'Used disk space on $1':
            row['disk_usage2'] = utilizacion_inm[key]

        elif key == 'RAM-used':
            row['ram2'] = utilizacion_inm[key]

        elif key == 'Outgoing network traffic on $1':
            row['out2'] = utilizacion_inm[key]

        elif key == 'CPU Usage':
            row['cpu2'] = utilizacion_inm[key]

        elif key == 'write.sda':
            row['write2'] = utilizacion_inm[key]

        elif key == 'iostat.sda':
            row['iops2'] = utilizacion_inm[key]

    dic_to_save[servicio] = row
    print(dic_to_save)

    with open('step_7.json','w') as f:
        json.dump(dic_to_save, f)
    
