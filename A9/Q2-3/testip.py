import re

testIP = '127.0.0.1'
#ip = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
ip = re.compile("^([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\." + "([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\." + "([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\." + "([01]?\\d\\d?|2[0-4]\\d|25[0-5])$")
result = ip.match(testIP)
if result:
   print testIP, " is a valid IP address"
else:
   print testIP, "is not a valid IP address"
