# from https://github.com/dddanmar/aws-iot-raspberry-pi-button/blob/master/mqtt_client.py
import paho.mqtt.client as mqtt
import ssl
import json
import time
import subprocess
import os

dir = os.path.dirname(os.path.realpath(__file__)) + '/'
certDir = dir + '../'
print certDir

p = subprocess.Popen (['python',dir+'scroll.py','Hello world'])
# print "starting process "+str(p.pid)

def on_connect(client, userdata, flags, rc):
    if rc != 0: 
        print("Connected with result code "+str(rc))
    client.subscribe("$aws/things/test-thing/shadow/update/accepted")

def on_message(client, userdata, msg):
    global p
    message_json = json.loads(str(msg.payload))
    print(message_json)
    
    try: 
      if message_json['state']['reported']['message']:
         message = message_json['state']['reported']['message']
         print message
         p.kill()
         p = subprocess.Popen (['python',dir + 'scroll.py',message])
         print "starting process "+str(p.pid)

    except KeyError:
      print "Invalid JSON received"

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.tls_set(ca_certs=certDir+'aws-iot-rootCA.crt', certfile=certDir+'cert.pem', keyfile=certDir+'privkey.pem', tls_version=ssl.PROTOCOL_SSLv23)
client.tls_insecure_set(True)
client.connect("A3KWJ0VBNKR8CV.iot.us-east-1.amazonaws.com", 8883, 60)
client.loop_forever()

