# to work with timestamps
import datetime
from readingdbmodif import get_items, get_trends, search_host, percentil, rank, mean, filter_time, db_connect
import json
import mysqldb


trends_items = ['CPU Usage']
history_items = ['iostat.sda', 'read.sda', 'write.sda', 'RAM-used', 'Used disk space on $1',
                 'Incoming network traffic on $1', 'Outgoing network traffic on $1']
'''
faltan por anadir los items de RAM,Capacidad, y red(ver problemas relacionados a estos)
'''


def hosts(name, start_time, end_time, user, passw, db_addr):
    st = start_time.timestamp()
    et = end_time.timestamp()
    trends_item_id = []
    history_item_id = []
    host_list = search_host(name)

    hosts_ids = [e[0] for e in host_list]

    select = hosts_ids[0]

    items_list = get_items(int(select))
    for i in range(len(trends_items)):
        trends_item_id.append(0)

    for i in range(len(history_items)):
        history_item_id.append(0)

    for i in items_list:
        if i[2] in trends_items:
            index = trends_items.index(i[2])
            trends_item_id[index] = i[1]
        elif i[2] in history_items:
            index = history_items.index(i[2])
            if history_item_id[index] == 0:
                history_item_id[index] = i[1]

    print(history_item_id)

    filtered = filter_time(st, et, trends_item_id)

    hist_dic = {}
    values = []
    data = mysqldb.main(st, et, history_item_id, user, db_addr, passw)
    for item, value_list in zip(history_items, data):
        num_max = mean([E[0] for E in value_list])
        num_avg = mean([E[1] for E in value_list])
        hist_dic[item] = {'Average_max': num_max, 'Average_avg': num_avg}

    dic = {}
    for i, item in zip(filtered, trends_items):
        numbers_max = [sample[3] for sample in i]
        num_max = mean(numbers_max)

        numbers_avg = [sample[2] for sample in i]
        num_avg = mean(numbers_avg)

        numbers_min = [sample[1] for sample in i]
        num_min = mean(numbers_min)

        score_max = [sample[3] for sample in i]
        score_max.sort()
        p_max = percentil(score_max)
        ans_max = rank(score_max, p_max, 0.95)

        score_avg = [sample[2] for sample in i]
        score_avg.sort()
        p_avg = percentil(score_avg)
        ans_avg = rank(score_avg, p_avg, 0.95)

        score_min = [sample[1] for sample in i]
        score_min.sort()
        p_min = percentil(score_min)
        ans_min = rank(score_min, p_min, 0.95)

        '''
        ir incrementando el diccionario dic de la forma dic={item_id:{'Average max':num_max,'Average avg':num_avg,..... }....}
        '''
        dic[item] = {'Average_max': num_max, 'Average_avg': num_avg}
    dic.update(hist_dic)
    return dic
