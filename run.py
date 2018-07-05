#Imports
import eel
from save_load import *
from functions import *

#
eel.init('web')

@eel.expose
def save(table,lista):
	result = func_save(table,lista)
	return result


@eel.expose
def load(table_list):
	result = func_load(table_list)
	return result

@eel.expose
def delete(table,selected):
	result = func_del(table,selected)
	print(result)
	return result











eel.start('lilipad1.html')


