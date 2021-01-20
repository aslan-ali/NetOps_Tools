from netmiko import ConnectHandler
from getpass import getpass

username=input('Username: ')
password=getpass()

cisco_r1={
    "device_type":"cisco_xe",
     "ip": "10.10.20.48",
     "username": username,
     "password": password
}

net_connect=ConnectHandler(**cisco_r1)

config_commands=['int loopback55',' ip add 1.1.1.1 255.255.255.255']
output=net_connect.send_config_set(config_commands)
print(output)
