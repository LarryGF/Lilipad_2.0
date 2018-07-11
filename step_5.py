import json,os
import zabixmaster as zb
import opennebula 
import datetime
from readingdbmodif import percentil,rank,mean
from step_6 import *
from step_7 import *

mb = ['Incoming network traffic on $1','Outgoing network traffic on $1','RAM-used','Used disk space on $1']

cont=0

def l5(table_name):
    for root,dirs,files in os.walk(os.getcwd()):
        for file in files:
            if file == str(table_name)+'.json':
                path = os.path.join(root,file)
                
            # try:
                with open(path) as f:
                    dic = json.load(f)
                return dic
                
            

 
def step5 (servicio,user,passw,db_addr,st,et):
    start_time=datetime.datetime.strptime(st,'%d/%m/%Y')
    end_time=datetime.datetime.strptime(et,'%d/%m/%Y')
    # start_time= datetime.datetime(2018,5,24)
    # end_time= datetime.datetime(2018,5,31)
    values_avg = []
    max_values = []
    step6_sum = {}
    os.makedirs(os.path.join(os.getcwd(),'step5',servicio),exist_ok = True)
    os.makedirs(os.path.join(os.getcwd(),'step6'),exist_ok = True)
    dic4={}
     
    dic = l5('tab_serv')
    # print(dic)######cambiar esto para llamar a la tabla del paso 2
    for row in dic.keys():
    	Index = {}
    	if dic[row]['service'] == servicio:
            with open('parser.json') as f:
                parse = json.load(f)
                
            zabbix_id = parse[dic[row]['vmachine']]
            print(zabbix_id)
            # print(zabbix_id)
            
            now = start_time##Falta por definir
            # print('Now:',now)
            delta = datetime.timedelta(1)
            # print('delta:',delta)
            zb.db_connect(user,passw,db_addr)
            
            while now<=end_time:
                dic2=zb.hosts(zabbix_id,now,now+delta)
                dic4[now.timestamp()]=dic2
                now +=delta
            
            item_names = [each_dic.keys() for each_dic in dic4.values()][0]
            days = dic4.keys()##Lista con dias a itera
            for item_name in item_names:
                #print(item_name)
                values_avg=[]
                max_values=[]
                for day in days: 
                    if day!='Index':
                        # print(dic4[day][item_name]['Average_avg'])
                        values_avg.append(dic4[day][item_name]['Average_avg'])
                        #print(len(values_avg))
                        # print(values_avg,end='\n\n')
                        max_values.append(dic4[day][item_name]['Average_max'])
                        #print(len(max_values))
                # print(max_values,end='\n\n')
                avg = mean(values_avg)
                perc = percentil(sorted(max_values))
                perc_max = rank(sorted(max_values), perc, 0.95)
                asignacion=opennebula.onevm(dic[row]['vmachine'])
                if item_name in mb:
                	avg_avg = round(float(avg/1000000),2)
                	ans_max = round(float(perc_max/1000000),2)
                else:
                	avg_avg = round(avg,2)
                	ans_max = round(perc_max,2)
                Index[item_name]={'Asignacion':asignacion[item_name],'Avg_avg':avg_avg,'Percentil_max':ans_max}
    
                if item_name in step6_sum:
                    ##Realizar sumatoria de los valores de cada item de todas las VM pertenecientes a un servicio
                    if 'Avg_avg' and 'Percentil_max' and 'Asignacion' in step6_sum[item_name]:
                        step6_sum[item_name]['Avg_avg'] += avg_avg
                        step6_sum[item_name]['Percentil_max'] += ans_max
                        if str(step6_sum[item_name]['Asignacion']) != 'no limitado': 
                            step6_sum[item_name]['Asignacion'] += asignacion[item_name]
                        else: pass
                        
                    else:
                        step6_sum[item_name]['Avg_avg'] = avg_avg
                        step6_sum[item_name]['Percentil_max'] = ans_max
                        step6_sum[item_name]['Asignacion'] = asignacion[item_name]
                        
                else:
                    step6_sum = Index.copy()
            ##Estructura de dic4:
            ## dic4 = {day:{item_name:{'Average max':num_max,'Average avg':num_avg,'95 percentile max':ans_max}},Index:{'Avg_avg':avg_avg,'Percentil_max':ans_max}}
            dic4['Index']=Index

            with open ('{}.json'.format(os.path.join(os.getcwd(),'step5',servicio,dic[row]['vmachine'])),'w') as f:
                ##Guardar en dir step5, archivo con nombre de la VM, conteniendo los valores de cada item por dia
                json.dump(dic4,f)
            with open ('{}.json'.format(os.path.join(os.getcwd(),'step6',servicio)),'w') as f:
                ##Guardar en directorio step6, archivo con nombre del servicio conteniendo la sumatoria descrita anteriormente
                json.dump(step6_sum,f)
            print(Index)
            print('success')
    load_step6(servicio)
    step7(servicio)
    return 'Finished'
