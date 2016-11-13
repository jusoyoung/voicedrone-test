import paho.mqtt.client as mqtt
import ssl, sys
from conf import *

def on_connect(mqttc, obj, flags, rc):
	if rc==0:
		print ("Subscriber Connection status code: "+str(rc)+" | Connection status: successful")
	elif rc==1:
		print ("Subscriber Connection status code: "+str(rc)+" | Connection status: Connection refused")

'''
fd = open(cert_file, 'r')
fd2 = open(key_file, 'r')
fd3 = open(root_cert, 'r')
print fd.readlines()
print fd2.readlines()
print fd3.readlines()
'''

mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.tls_set(root_cert, 
		certfile=cert_file, 
		keyfile=key_file, 
		cert_reqs=ssl.CERT_REQUIRED, 
		tls_version=ssl.PROTOCOL_SSLv23, 
		ciphers=None)






