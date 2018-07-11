import os
import json


def load_step6(servicio):
    '''
    Cargar dict = {VM_name:Indice}, donde indice es un dict con los valores por item
    '''

    vm_values = {}
    for root, dirnames, files in os.walk(os.path.join(os.getcwd(), 'step5', servicio)):
        for file in files:
            path = os.path.join(root, file)
            with open(path) as f:
                dic = json.load(f)
                indice = dic['Index']
            vm_values[file.strip('.json')] = indice

    with open('{}.json'.format(os.path.join(os.getcwd(), 'step6', servicio)), 'r') as f:
        sumatoria = json.load(f)

    vm_values['Sumatoria'] = sumatoria
    with open('tab_serv.json', 'r') as f:
        dic2 = json.load(f)

    dict_to_send = {}

    for vm in vm_values:
        row = {}
        row['service'] = servicio
        row['mv'] = vm
        for val in dic2.values():
            if val['vmachine'] == vm:
                row['subservice'] = val['subservice']

        temp_dic = vm_values[vm]
        for key in temp_dic:
            if key == 'read.sda':
                for value in temp_dic[key]:
                    if value == 'Avg_avg':
                        uprom_r = temp_dic[key][value]
                        row['uprom_r'] = uprom_r

                    elif value == 'Asignacion':
                        read_asigned = temp_dic[key][value]
                    elif value == 'Percentil_max':
                        umax_r = temp_dic[key][value]
                        row['umax_r'] = umax_r

            elif key == 'write.sda':
                for value in temp_dic[key]:
                    if value == 'Avg_avg':
                        uprom_w = temp_dic[key][value]
                        row['uprom_w'] = uprom_w
                    elif value == 'Asignacion':
                        write_asigned = temp_dic[key][value]
                    elif value == 'Percentil_max':
                        umax_w = temp_dic[key][value]
                        row['umax_w'] = umax_w

            elif key == 'iostat.sda':
                for value in temp_dic[key]:
                    if value == 'Avg_avg':
                        thru_uprom = temp_dic[key][value]
                        row['thru_uprom'] = thru_uprom
                    elif value == 'Asignacion':
                        thru_asigned = temp_dic[key][value]
                        row['thru_asigned'] = thru_asigned
                    elif value == 'Percentil_max':
                        thru_umax = temp_dic[key][value]
                        row['thru_umax'] = thru_umax

            elif key == 'Incoming network traffic on $1':
                for value in temp_dic[key]:
                    if value == 'Avg_avg':
                        rx_uprom = temp_dic[key][value]
                        row['rx_uprom'] = rx_uprom
                    elif value == 'Asignacion':
                        rx_asigned = temp_dic[key][value]
                        row['rx_asigned'] = rx_asigned
                    elif value == 'Percentil_max':
                        rx_umax = temp_dic[key][value]
                        row['rx_umax'] = rx_umax

            elif key == 'Outgoing network traffic on $1':
                for value in temp_dic[key]:
                    if value == 'Avg_avg':
                        tx_uprom = temp_dic[key][value]
                        row['tx_uprom'] = tx_uprom
                    elif value == 'Asignacion':
                        tx_asigned = temp_dic[key][value]
                        row['tx_asigned'] = tx_asigned
                    elif value == 'Percentil_max':
                        tx_umax = temp_dic[key][value]
                        row['tx_umax'] = tx_umax

            elif key == 'Used disk space on $1':
                for value in temp_dic[key]:
                    if value == 'Avg_avg':
                        use_avg = temp_dic[key][value]
                    elif value == 'Asignacion':
                        asigned = temp_dic[key][value]
                        row['asigned'] = asigned
                    elif value == 'Percentil_max':
                        use = temp_dic[key][value]
                        row['use'] = use

            elif key == 'RAM-used':
                for value in temp_dic[key]:
                    if value == 'Avg_avg':
                        ram_uprom = temp_dic[key][value]
                        row['ram_uprom'] = ram_uprom
                    elif value == 'Asignacion':
                        ram_asigned = temp_dic[key][value]
                        row['ram_asigned'] = ram_asigned
                    elif value == 'Percentil_max':
                        ram_umax = temp_dic[key][value]
                        row['ram_umax'] = ram_umax

            elif key == 'CPU Usage':
                for value in temp_dic[key]:
                    if value == 'Avg_avg':
                        cpu_uprom = temp_dic[key][value]
                        row['cpu_uprom'] = cpu_uprom
                    elif value == 'Asignacion':
                        cpu_asigned = temp_dic[key][value]
                        row['cpu_asigned'] = cpu_asigned
                    elif value == 'Percentil_max':
                        cpu_umax = temp_dic[key][value]
                        row['cpu_umax'] = cpu_umax

        dict_to_send[vm] = row

    with open('tab_ut_serv.json', 'w') as file:
        json.dump(dict_to_send, file)
    file.close()
