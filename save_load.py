import json
import os

os.makedirs('data', exist_ok=True)
data_dir = os.path.join(os.path.abspath('.'),'data')


def func_save(table,lista):
	'''
	Takes a list of dictionary and it transforms it to a dictionary of dictionaries, and then it saves
	that dictionary as a .json file
	'''
	
	dic = {}
	for index,dictionary in enumerate(lista):
		dic[index+1] = dictionary
		dic[index+1]['id'] = index +1
	try:
		with open(os.path.join(data_dir,'{}.json').format(table),'w') as f:
			json.dump(dic,f)
		return True

	except Exception as e:
		return e







def func_load(table_list):
	'''
	Returns all tables in a list in the same order they were asked.
	Example: func_load('existentes','futuros') --> [[{list for 'existentes'},{..}],[{list for 'futuros'},{..}]]
	'''
	

	list_to_send = []
	
	for element in table_list:
		
		try:
			with open(os.path.join(data_dir,'{}.json').format(element)) as f:
				lista = []
				
				dic = json.load(f)

				# 	file = open(os.path.join(data_dir,'{}.json').format(element),'w')
				# 	file.write('{}')
				# 	file.close()
				# 	dic = {}

				if dic.keys():
					for fila in sorted(dic.keys()): 
						lista.append(dic[fila])
				else:
					pass
			

			list_to_send.append(lista)

		except:
			list_to_send.append([])
	
	return list_to_send