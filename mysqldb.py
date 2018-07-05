import mysql.connector as mysql
import datetime


def connect(user,host,password,database):
	conn = mysql.connect(user=user,host=host, password=password,database=database)
	cursor = conn.cursor()
	return conn,cursor
def execute(cursor,itemid_list,start_time,end_time):
	item_values = []
	for item in itemid_list:
		cursor.execute('select value_max,value_avg from trends_uint where itemid=%s and clock>=%s and clock<=%s;'%(item,start_time,end_time))
		data = cursor.fetchall()
		item_values.append(data)
	# for tupla in data:
	# 	values_max.append(tupla[2])
	# 	value_avg.append(tupla[3])
	return item_values
def close(conn):
	conn.close()

def main(start_time,end_time,itemid_list,user='zabbixinfo',host='10.8.9.164',password='1234',database='zabbix'):
	conn,cursor=connect(user,host,password,database)
	value_list= execute(cursor,itemid_list,start_time,end_time)
	close(conn)
	return value_list

if __name__ == "__main__":
	start_time = datetime.datetime(2017,9,1,8).timestamp()
	end_time = datetime.datetime(2017,11,4,16).timestamp()
	a = main(start_time,end_time,[28446,28463])
	print(a)

