# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 01:27:33 2020

@author: Tejas

https://www.google.com/settings/security/lesssecureapps  - Enable this to make the code run
"""


############### Python code to send fake emails with fake names 
fromreal = 'tejas.krishnareddy1415@gmail.com'
victim = "aravindk3011@gmail.com"
victim_name = 'Mayukh'    ## 'me'

import yagmail
yag=yagmail.SMTP({fromreal:victim_name}, 'Tejtkreddy@33') 

yag.send(victim, "Shoot Properly Bro", "Tejas is Awesome!! You know that right")



################## Python code to display all wifi names in the range
import subprocess

results = subprocess.check_output(["netsh", "wlan", "show", "network"])
results = results.decode("ascii")
results = results.replace("\r","")
ls = results.split("\n")
ls = ls[4:]
ssids = []
x = 0
while x < len(ls):
    #if x % 5 ==0:     ### to get only the names
        ssids.append(ls[x])
        x += 1
print(ssids)



### Print some mac addresses
from netifaces import interfaces, ifaddresses, AF_INET
for ifaceName in interfaces():
    addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
    print ('%s: %s' % (ifaceName, ', '.join(addresses)))





#### Get my own local ip address
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 1))  # connect() for UDP doesn't send packets
local_ip_address = s.getsockname()[0]







