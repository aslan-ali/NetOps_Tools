'''
For commands in cisco device for example ospf static route and interface configuration with format(old_method_string)


public_ip=input("Public IP: ")
private_ip=input("Private IP: ")

configuration="""
interface gigabitethernet0/1
ip address {public_ip} 255.255.255.0
no shutdown
interface gigabitethernet 0/0
ip address {private_ip} 255.255.255.0
no shutdown
ip route {public_ip} 255.255.255.255 85.132.88.1
router ospf 1
network {private_ip} 0.0.0.0 area 0
ispf"""

template=configuration.format(public_ip=public_ip, private_ip=private_ip)
print(template)
