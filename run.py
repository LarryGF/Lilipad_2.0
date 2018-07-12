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
    return result


@eel.expose
def tools(data):
    result = func_tools(data)
    return result


@eel.expose
def usage(data):
    result = func_usage(data)
    return result

@eel.expose
def map(data):
    result = func_map(data)
    return result


eel.start('index.html', options={'port': 8686})
