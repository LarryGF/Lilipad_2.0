
def step_4(dic):		###diccionario con servicio y argumentos
	if dic['servicio']=='correo':
		import correo
		##el orden de los argumentos es:ruta,mes/dia
		correo.main(dic['ruta'],dic['fecha'])
		return "El archivo 'general_data.csv' esta listo con sus datos"		
	elif dic['servicio']=='navegacion':
		print(dic)
		import QoE
		##el orden de los argumentos es: ruta,lista de usuarios,start_time,end_time
		QoE.main(dic['ruta'],dic['users_list'],dic['start_time'],dic['end_time'])
		return "El archivo data.txt esta listo con sus datos"



