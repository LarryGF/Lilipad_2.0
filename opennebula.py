import re,subprocess
##MEMORY
##SIZE
def onevm(vm_name):
	dic = {}
	with subprocess.Popen(['sshpass','-p','opennebula_manager*','ssh','root@10.8.9.189','onevm','show',vm_name,'--all'],stdout = subprocess.PIPE) as p:
		# print('Opennebula')
		output = p.stdout.read().decode()
		# print(output)
	patt1 = re.compile('VCPU="(.+)"')
	patt2 = re.compile('MEMORY="(.+)"')
	patt3 = re.compile(r'\s+(SIZE="(.+)")')
	VCPU = patt1.search(output)
	MEMORY = patt2.search(output)
	SIZE = patt3.search(output)
	# print(VCPU.group(1))
	# print(MEMORY.group(1))
	# print(SIZE.group(2))
	dic={'CPU Usage': float(VCPU.group(1)),'RAM-used':float(MEMORY.group(1)),'Used disk space on $1':float(SIZE.group(2)),'iostat.sda':'no limitado','read.sda':'no limitado','write.sda':'no limitado','Outgoing network traffic on $1':'no limitado','Incoming network traffic on $1':'no limitado'}
	return dic
