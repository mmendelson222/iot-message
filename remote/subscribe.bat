rem @echo off

rem an arbitrary feed. 
set thing=test-thing
set certslocation=..\..\
set endpoint=A3KWJ0VBNKR8CV.iot.us-east-1.amazonaws.com

start "rejected" "\Program Files (x86)\mosquitto\mosquitto_sub.exe" --cafile "%certslocation%VeriSign-Class%%203-Public-Primary-Certification-Authority-G5.pem.txt" --cert "%certslocation%cd5d235b0b-certificate.pem.crt" --key "%certslocation%cd5d235b0b-private.pem.key" -h %endpoint% -p 8883 -q 1 -d -t $aws/things/%thing%/shadow/update/rejected 

start "accepted" "\Program Files (x86)\mosquitto\mosquitto_sub.exe" --cafile "%certslocation%VeriSign-Class%%203-Public-Primary-Certification-Authority-G5.pem.txt" --cert "%certslocation%cd5d235b0b-certificate.pem.crt" --key "%certslocation%cd5d235b0b-private.pem.key" -h %endpoint% -p 8883 -q 1 -d -t $aws/things/%thing%/shadow/update/accepted



:end