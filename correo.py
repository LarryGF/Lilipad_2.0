import re
import csv
import subprocess
import sys
import getpass
from operator import itemgetter

local = "relay=local"
sents_delays = []
emails_send = 0
first_errors_id_list = []
month_dict = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'Jun', '07': 'Jul', '08': 'Aug',
              '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
error_causes_list = []


def to_line_process():
    cont2 = emails_send
    if struct_line[11] == 'status=sent' and struct_line[5][0:-1] not in first_errors_id_list and float(
            struct_line[8][6:-1]) < 3600.0:
        sents_delays.append(float(struct_line[8][6:-1]))
        cont2 += 1
    elif struct_line[11] == 'status=deferred' and float(struct_line[8][6:-1]) < 3600.0:
        if struct_line[5][0:-1] not in first_errors_id_list:
            first_errors_id_list.append(struct_line[5][0:-1])
            error_cause = error_identificator()
            error_causes_list.append(error_cause)
    return cont2


# calculo del promedio del delay
def avg_delay():
    avg = sum(sents_delays) / len(sents_delays)
    return avg


# se encargara de por cada uno de los errores,darle seguimiento al error en el archivo y almacenar los datos
def errors_lines_process(file_route):
    error_cause_index = 0
    for id in first_errors_id_list:
        number_of_retries = 0
        error_cause = " "
        delay = 0
        final_status = " "
        error_cause = error_causes_list[error_cause_index]
        error_cause_index += 1
        file2 = open(file_route, 'r')
        for linea in file2:
            struct_line = linea.split(' ')
            for i in struct_line:
                if len(i) == 0:
                    struct_line.remove(i)
            if struct_line[0] == month2 and struct_line[1] == day and int(struct_line[2][0:2]) >= 11 and int(
                    struct_line[2][0:2]) < 22:
                try:
                    if struct_line[6].startswith('to=') and struct_line[7] != local and struct_line[5][0:-1] == id:
                        if struct_line[11] == 'status=sent':
                            delay = struct_line[8][6:-1]
                            final_status = "sent"
                            number_of_retries += 1
                            break
                        elif struct_line[11] == 'status=deferred':
                            number_of_retries += 1
                            final_status = "not sent"
                            delay = struct_line[8][6:-1]
                except IndexError:
                    pass
        datos.writerow(
            [id, delay, final_status, number_of_retries, error_cause])
        file2.close()


def error_identificator():
    # determinar el tipo de error,esto se podria mejorar,incluyendo un diccionario con cada tipo de error,para no tener tantos if,solo que no se encontro una relacion donde estuvieran todas las posibles respuestas del servidor con su significado

    if struct_line[10] == 'dsn=4.0.0,':
        if struct_line[15] == '450':
            error = 'Internal system error'
        elif struct_line[15] == '452':
            error = 'Message would exceed mailbox quota'
        elif struct_line[15] == '400':
            error = 'Building greylist'
        elif struct_line[15] == '451':
            error = 'Suspicious message, please come back later'
        elif struct_line[15] == '421':
            error = 'Maximum mail limit exceeded'
        elif struct_line[16].startswith('(del') or struct_line[14].startswith('refu') or struct_line[12].startswith(
                '(del'):
            error = 'No SMTP service due to policy restriction'
        else:
            error = 'unknown error'
            print(struct_line)
    elif struct_line[10] == 'dsn=4.4.1,':
        if struct_line[15] == 'No' and struct_line[16] == 'route':
            error = 'No route to host'
        elif struct_line[16] == 'timed' or struct_line[12].startswith('(del'):
            error = 'Connection timed out'
        elif struct_line[16].startswith('ref'):
            error = 'Connection refused'
        else:
            error = 'unknown error'
            print(struct_line)
    elif struct_line[10] == 'dsn=4.1.8,':
        error = 'Sender address rejected,Domain not found'
    elif struct_line[10] == 'dsn=4.5.3,':
        error = 'Too many recipients'
    elif struct_line[10] == 'dsn=4.4.2,':
        error = 'Conversation time out while sending mail'
    elif struct_line[10] == 'dsn=4.7.0,' and struct_line[15] == '421':
        error = 'Too many errors'
    elif struct_line[10] == 'dsn=4.7.0,':
        error = 'Message suspicious due to very low reputation of the sending IP address'
    elif struct_line[10] == 'dsn=4.7.1,':
        error = 'Relay acces denied'
    elif struct_line[10] == 'dsn=4.2.0,':
        error = 'Recipient address rejected:Greylisted'
    elif struct_line[10] == 'dsn=4.4.3,':
        error = 'Host or domain name not found'
    elif struct_line[10] == 'dsn=4.3.2,':
        error = 'Service currently unavailable'
    elif struct_line[10] == 'dsn=4.1.0,':
        error = 'Spamprotection is on,please resend your email'
    elif struct_line[10] == 'dsn=4.2.2,':
        error = 'User is receiving mail too quickly'
    elif struct_line[10] == 'dsn=4.3.5,':
        error = 'Recipient address rejected:Server configuration error'
    elif struct_line[10] == 'dsn=4.2.1,':
        error = 'The user you are trying to contact is receiving mail at a rate that prevents additional messages from being delivered'
    elif struct_line[10] == 'dsn=4.3.0,':
        error = 'First-time sender tempfailed as anti-spam measure'
    elif struct_line[10] == 'dsn=4.1.7,':
        error = 'Sender address rejected:unverified address'
    elif struct_line[10] == 'dsn=4.7.25,':
        error = 'Client host rejected:cannot find your hostname'
    else:
        error = 'unknown error'
        print(struct_line)
    return error


def main(file_route, date):
    global month2
    global struct_line
    global datos
    global emails_send
    month = (date[0:2])
    month2 = month_dict[month]
    global day
    day = date[2:4]
    print('checking')
    if day.startswith('0'):
        day = day[1]
    print('opening log')
    file = open(file_route, 'r')
    for linea in file:
        struct_line = linea.split(' ')
        for i in struct_line:
            if len(i) == 0:
                struct_line.remove(i)
        try:  # para quedarnos solo con lineas "to" y con relay != de local
            if struct_line[6].startswith('to=') and struct_line[7] != local and struct_line[0] == month2 and struct_line[
                    1] == day and int(struct_line[2][0:2]) >= 11 and int(struct_line[2][0:2]) < 22:
                emails_send = to_line_process()
        except IndexError:
            pass
    print('generating .csv')
    avg = round(avg_delay(), 3)
    csvdatos = open('general_data.csv', 'w', newline='')
    mail = csv.writer(csvdatos)
    mail.writerow(['avg delay', 'emails send', 'emails with errors'])
    mail.writerow([avg, emails_send, len(first_errors_id_list)])
    mail.writerow(['', '', ''])
    mail.writerow(['', '', ''])
    csvdatos.close()
    csvdatos = open('errors_report.csv', 'w', newline='')
    datos = csv.writer(csvdatos)
    datos.writerow(['email id', 'final delay', 'final status',
                    'number of retries', 'error cause'])
    errors_lines_process(file_route)
    csvdatos.close()
    print('generating errors report')
    file = open('errors_report.csv', 'r')
    dic = {}
    for line in file:
        error = line.split(',')
        if error[4] == 'error cause\n':
            pass
        else:
            if error[4] in dic:
                dic[error[4]] += 1
            else:
                dic[error[4]] = 1
    csvdatos = open('general_data.csv', 'a', newline='')
    per = csv.writer(csvdatos)
    per.writerow(['error_cause', 'number of errors', 'percentage of total'])
    for key, value in sorted(dic.items(), key=itemgetter(1), reverse=True):
        per.writerow([(key), value, round(
            value*100/len(first_errors_id_list), 3)])
    csvdatos.close()
    print('finishing method')
    return 'El archivo .csv esta listo'
