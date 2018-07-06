# Imports
import eel
from save_load import func_save, func_load
from functions import *

#
eel.init('web')


@eel.expose
def save(table, lista):
    result = func_save(table, lista)
    return result


@eel.expose
def load(table_list):
    result = func_load(table_list)
    return result


@eel.expose
def delete(table, selected):
    result = func_del(table, selected)
    print(result)
    return result


eel.start('index.html', options={'port': 8686})
