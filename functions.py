

def func_del(table, selected):
    # list_to_send = []
    list_id = []
    for dictionary in selected:
        list_id.append(dictionary['id'])

    for ident in list_id:
        for element in table:
            if int(ident) == int(element['id']):
                table.pop(table.index(element))

    return table


def func_tools(object):
    if object['name'] == "correo":
        import correo
        result = correo.main(object['ruta_mail'], object['date_mail'])

    elif object['name'] == 'navegacion':
        import QoE
        result = QoE.main(object['ruta_nav'],
                          object['usr_list'], object['date_nav_inf'], object['date_nav_sup'])

    return result


def func_usage(data):
    from step_5 import step5
    result = step5(data['service'], data['user'],
                   data['password'], data['ip'], data['date_start'], data['date_end'])
    return result


def func_map(data):
    from relation import relation_one, relation_prox
    result1 = relation_one(data['one']['one_pass'], data['one']['one_user'], data['one']
                           ['one_ip'], data['zabbix']['zabbix_user'], data['zabbix']['zabbix_pass'], data['zabbix']['zabbix_ip'], data['zabbix']['zabbix_db'])
    result2 = relation_prox(data['prox']['prox_pass'], data['prox']['prox_user'], data['prox']
                            ['prox_ip'], data['zabbix']['zabbix_user'], data['zabbix']['zabbix_pass'], data['zabbix']['zabbix_ip'], data['zabbix']['zabbix_db'])
    return result1, result2
