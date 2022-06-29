
import time
import machine
from network import WLAN


wlan = WLAN()
if machine.reset_cause() != machine.SOFT_RESET:
    wlan.init(mode=WLAN.STA)
    # configuration below MUST match your home router settings!!
    wlan.ifconfig(config=('192.168.10.50', '255.255.255.0', '192.168.10.1', '192.168.10.1')) # (ip, subnet_mask, gateway, DNS_server)

if not wlan.isconnected():
    # change the line below to match your network ssid, security and password
    wlan.connect('bub', auth=(WLAN.WPA2, 'Vac5mF3a'), timeout=5000)
    print("connecting",end='')
    while not wlan.isconnected():
        time.sleep(1)
        print(".",end='')
    print("connected")
