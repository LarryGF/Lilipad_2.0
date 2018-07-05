###imports


def func_del(table,selected):
	# list_to_send = []
	list_id = []
	for dictionary in selected:
		list_id.append(dictionary['id'])

	for ident in list_id:
		for element in table:
			if int(ident) == int(element['id']):
				table.pop(table.index(element))

	return table

