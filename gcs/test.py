import paho.mqtt.client as mqtt
from gcs_mqttc import mqttc, host, port, topic
import time

is_subscribed = False

""" Callback functions for mqtt client """
def on_subscribe(mqttc, obj, mid, granted_qos):
        print("Subscribed: "+str(mid)+" "+str(granted_qos)+"data"+str(obj))

        global is_subscribed
        is_subscribed = True

print "start!"

print host, port


mqttc.on_subscribe = on_subscribe
#mqttc.on_message = on_message
mqttc.connect(host, port)
print "connect done"
mqttc.loop_start()

while not is_subscribed:
       print "Waiting for subscribing..."
       mqttc.subscribe(topic, qos=1)
       time.sleep(1)


mqttc.loop_stop()
