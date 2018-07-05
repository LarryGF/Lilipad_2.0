import json

def step_1(users_dic):
	f=open('step_1.json','w')
	json.dump(users_dic,f)
	f.close()

def step_1_load():
	f=open('step_1.json')
	var = json.load(f)
	f.close()
	return var



#dic={'current_users': 34, 'new_users': 55, 'future_users': 79}
#step_1(dic)
