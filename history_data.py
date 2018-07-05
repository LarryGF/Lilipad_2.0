"""
Retrieves history data for a given numeric (either int or float) item_id
"""
###!!!Must uncomment pyzabbix
from pyzabbix import ZabbixAPI
from datetime import datetime
import time


def history_api(item_id,time_from,time_till):
  # The hostname at which the Zabbix web interface is available
  ZABBIX_SERVER = 'http://10.8.6.95/zabbix'
  zapi = ZabbixAPI(ZABBIX_SERVER)
  # Login to the Zabbix API
  zapi.login('Admin', 'zabbix')
  # print(item_id)
  # Create a time range
  # time_till = datetime.now().timestamp()#time.mktime(datetime.now().timetuple())
  # time_from = datetime(2018,5,17).timestamp()#time_till - 60 * 60 * 4  # 4 hours
  # time_till = time.mktime(datetime.now().timetuple())
  # time_from = time_till - 60 * 60 * 4  # 4 hours
  # item_id=29399
  # time_from=datetime(2018,5,23).timestamp()
  # print(datetime.fromtimestamp(time_from))
  # time_till=datetime(2018,5,24).timestamp()
  # print(datetime.fromtimestamp(time_till))
  # Query item's history (integer) data
  history = zapi.history.get(itemids=[item_id],
                             time_from=time_from,
                             time_till=time_till,
                             output='extend',
                             )

  # If nothing was found, try getting it from history (float) data
  if not len(history):
      history = zapi.history.get(itemids=[item_id],
                                 time_from=time_from,
                                 time_till=time_till,
                                 output='extend',
                                 history=0,
                                 )

  # Print out each datapoint
  # print(history)
  value_list=[]
  for point in history:
      # print("{0}: {1}".format(datetime.fromtimestamp(int(point['clock']))
      #                         .strftime("%x %X"), point['value']))
      
      value_list.append(int(point['value']))
  # print (value_list)
  return value_list    
# 

# history_api()