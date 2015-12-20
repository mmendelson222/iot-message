rem @echo off
if [%1]==[] (
@echo Usage: %0 ^<message^>
goto end
)

rem the following is defined in AWS iot
set thing=test-thing
set certslocation=..\..\
set endpoint=A3KWJ0VBNKR8CV.iot.us-east-1.amazonaws.com

echo message
echo %1

rem remove quotes if present.
set stripped=%1
if "%stripped:~0,1%%stripped:~0,1%" NEQ """" goto quotesRemoved
set stripped=%stripped:"=%
:quotesRemoved

"\Program Files (x86)\mosquitto\mosquitto_pub.exe" --cafile "%certslocation%VeriSign-Class%%203-Public-Primary-Certification-Authority-G5.pem.txt" --cert "%certslocation%cd5d235b0b-certificate.pem.crt" --key "%certslocation%cd5d235b0b-private.pem.key" -h %endpoint% -p 8883 -q 1 -d -t $aws/things/%thing%/shadow/update -m "{ \"state\": {\"reported\": {\"message\": \"%stripped%\" } } }"

:end


