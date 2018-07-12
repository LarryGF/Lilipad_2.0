import re,subprocess
import mysql.connector as mysql
import json

def relation_prox(password_prox, user_prox, ip_prox,user_zabbix,password_zabbix, ip_zabbix,database_zabbix):
	
	
	with subprocess.Popen(['sshpass','-p',password_prox,'ssh',user_prox + "@" + ip_prox,'pct', 'list'],stdout = subprocess.PIPE) as l:
		output0 = l.stdout.read().decode()
	print("---------------------------------------CONTENEDORES (y su estado) EXISTENTES EN PROXMOX------------------------------------------------------------------")
	print(output0)
	print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
	
	pattern = re.compile(r'(\d\d\d)')
	id_list = re.findall(pattern,output0) 
	
	dic={}
	ip_list = []
	for i in id_list:
		with subprocess.Popen(['sshpass','-p',password_prox,'ssh',user_prox + "@" + ip_prox ,'pct','config', i ],stdout = subprocess.PIPE) as p:
			output = p.stdout.read().decode()
		patt1 = re.compile(r'ip=(.*)/')
		new = patt1.search(output)
		IP_PROX=new.group(1)
		dic["id"]=i
		dic["ip"]=IP_PROX	
		ip_list.append(dic)
		dic={}
	print("---------------------------------------RELACION ID DEL CONTENEDOR DEL PROXMOX CON SU IP------------------------------------------------------------------")
	print(ip_list)
	print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
	
	
	name_zabbix = []
	hostid_values = []
	ip_no_monitorizados=[]
	name_hostid=[]
	conn = mysql.connect(user=user_zabbix , password=password_zabbix, host=ip_zabbix ,database=database_zabbix)
	cursor = conn.cursor(buffered=True)

	for i in ip_list:
	
		cursor.execute('select hostid from interface where ip="%s";'%i["ip"])        
		data = cursor.fetchone()
		if str(data)=='None':
			ip_no_monitorizados.append(i["ip"])	
		else:
			dic["id"]=i["id"]
			dic["hostid"]=str(data[0])
			name_hostid.append(dic)
		dic={}	

	print("---------------------------------------ID DE PROXMOX CON HOSTID DE ZABBIX------------------------------------------------------------------")
	print(name_hostid)
	print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
	print("---------------------------------------IP QUE NO SE ESTAN MONITORIZANDO EN ZABBIX------------------------------------------------------------------")
	print(ip_no_monitorizados)
	print("-----------------------------------------------------------------------------------------------------------------------------------------------------")

	nameprox_namezbbbx=[]	
	for i in name_hostid :
		cursor.execute('select name from hosts where hostid="%s";'%i["hostid"])        
		data = cursor.fetchone()

		dic["id_prox"]=i["id"]
		dic["name_zabbix"]=str(data[0])
		nameprox_namezbbbx.append(dic)
		dic={}
	
	print("-----------------------------------------------ID EN PROXMOX Y NOMBRE DE ZABBIX DE LA MISMA INSTANCIA VIRTUAL-----------------")
	print(nameprox_namezbbbx)
	
	print("-----------------------------------------------------------------------------------------------------------------------------------------------------")

	try:
		f = open("parser.json")
	except:
		f = open("parser.json", "w")
		f.write('{}')
		f.close()
		f = open("parser.json")

	var=json.load(f)
	for i in nameprox_namezbbbx:
		var[i["id_prox"]]=i['name_zabbix']
	print(var)
	f=open("parser.json","w")
	json.dump(var,f)
	f.close()
	print('Finished Prox')
	return 'Success Prox'

# relation_prox("team_manager*", "root", "10.8.9.202","zabbixinfo","1234", "10.8.6.164","zabbix")



	
def relation_one(password_one, user_one, ip_one,user_zabbix,password_zabbix,ip_zabbix,database_zabbix):
	
	
	with subprocess.Popen(['sshpass','-p',password_one,'ssh',user_one + "@" + ip_one,'onevm', 'list'],stdout = subprocess.PIPE) as l:
		output0 = l.stdout.read().decode()

	file=open("text","w")
	file.write(output0)
	file.close()
	file=open("text")
	salida =file.read()
	row_list = salida.split('\n')	
	file.close()
	dic={}
	list_dict = []
	for row in row_list:
		try:
			if row.split()[4]=="runn" or row.split()[4]=="poff" or row.split()[4]=="stop":
				dic['name']=row.split()[3]
				list_dict.append(dic)
				dic={}
			else:
				dic['name']=row.split()[3]+" "+row.split()[4]
				list_dict.append(dic)
				dic={}
		except Exception as e:
			print(e)

	print("---------------------------------------NOMBRES DE LAS INSTANCIAS VIRTUALES DE OPENNEBULA------------------------------------------------------------------")
	print(list_dict)
	print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
	
	dic_ip_name={}
	lista_ip = []
	for i in list_dict:
		try:
			with subprocess.Popen(['sshpass','-p',password_one,'ssh',user_one + "@" + ip_one ,'onevm','show','"'+i["name"]+'"','--all' ],stdout = subprocess.PIPE) as 	p:
				output = p.stdout.read().decode()

			patt1 = re.compile(r'IP="(.*)"')
			new = patt1.search(output)
			IP_ONE=new.group(1)
			dic_ip_name["ip"]=IP_ONE
			dic_ip_name["name"]=i["name"]
			lista_ip.append(dic_ip_name)
			dic_ip_name={}
		except:
			pass
	print("---------------------------------------IP DE OPENNEBULA CON NOMBRE DE OPENNEBULA------------------------------------------------------------------")

	print(lista_ip)
	print("-----------------------------------------------------------------------------------------------------------------------------------------------------")



	dic={}
	name_zabbix = []
	name_hostid= []
	ip_no_monitorizados=[]
	conn = mysql.connect(user=user_zabbix , password=password_zabbix, host=ip_zabbix ,database=database_zabbix)
	cursor = conn.cursor(buffered=True)

	for i in lista_ip:
	
		cursor.execute('select hostid from interface where ip="%s";'%i["ip"])        
		data = cursor.fetchone()
		if str(data)=='None':
			ip_no_monitorizados.append(i)	
		else:
			dic["name"]=i["name"]
			dic["hostid"]=str(data[0])
			name_hostid.append(dic)
		dic={}
	print("---------------------------------------NOMBRE DE OPENNEBULA CON HOSTID DE ZABBIX------------------------------------------------------------------")
	print(name_hostid)
	print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
	print("---------------------------------------IP QUE NO SE ESTAN MONITORIZANDO EN ZABBIX------------------------------------------------------------------")
	print(ip_no_monitorizados)
	print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
	
	dic={}
	nameone_namezbbbx=[]	
	for i in name_hostid :
		cursor.execute('select name from hosts where hostid="%s";'%i["hostid"])        
		data = cursor.fetchone()

		dic["name_one"]=i["name"]
		dic["name_zabbix"]=str(data[0])
		nameone_namezbbbx.append(dic)
		dic={}
	print("-----------------------------------------------NOMBRE EN OPENNEBULA Y NOMBRE DE ZABBIX DE LA MISMA INSTANCIA VIRTUAL-----------------")
	print(nameone_namezbbbx)
	
	print("-----------------------------------------------------------------------------------------------------------------------------------------------------")

	try:
		f = open("parser.json")
	except:
		f = open("parser.json", "w")
		f.write('{}')
		f.close()
		f = open("parser.json")

	var=json.load(f)
	for i in nameone_namezbbbx:
		var[i["name_one"]]=i['name_zabbix']
	print(var)
	f=open("parser.json","w")
	json.dump(var,f)
	f.close()
	print('finished one')
	return 'Success ONE'

# relation_one("opennebula_manager*", "root", "opennebula.cujae.edu.cu","zabbixinfo","1234","10.8.6.164","zabbix")

