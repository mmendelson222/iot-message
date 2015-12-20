# iot-message
Python code to receive a message from AWS iot, using MQTT, and display it on an OLED device.  Some assembly required. 

##Setup for Raspberry pi
* use git to download this code
* move iot-messages to /etc/init.d
* edit the file /etc/rc.d/rc.local and add the following line: /etc/init.d/iot-messages start
* add the certificate files necessary for MQTT to the directory /home/pi, and make sure they have the names aws-iot-rootCA.crt, privkey.pem and cert.pem 
* edit the file iot-message.py and change the endpoint to the appropriate value. 

##Notes
The way this works is that the main executable, iot-message.py, listens for updates and will start the process necessary to display text on the OLED device (scroll.py).  It would be straightforward to replace scroll.py if you have another device you want to use. 

In the course of starting and stopping this app, all python processes will be killed (see iot-messages).  So if you're doing anything else with your pi, you have been warned!
