import yaml
from netmiko import ConnectHandler
import time
print("Hello Guys, Welcome to my Script,You will see some configuration on specific router\n")
hello= input("Do you want BGP or Ospf or Static: ")

if hello == "bgp" :
    with open("bgp.yaml") as file1:
        data1 =yaml.full_load(file1)
    from jinja2 import Environment, FileSystemLoader
    env = Environment(loader=FileSystemLoader("."))
    temp = env.get_template("bgp.j2")
    R1 = temp.render(int=data1)
    vxr = ConnectHandler(host="192.168.8.135", username="eslam", password="eslam", device_type="cisco_ios")
    vxr.enable()
    vxr.config_mode()
    vxr.send_command_timing(R1)
    show = vxr.send_command_timing("do show bgp summary")
    print(show)
elif hello == "ospf" :
    with open("ospf.yaml") as file2:
        data2 =yaml.full_load(file2)
    from jinja2 import Environment, FileSystemLoader
    env = Environment(loader=FileSystemLoader("."))
    temp = env.get_template("ospf.j2")
    R2 = temp.render(int=data2)
    vxr = ConnectHandler(host="192.168.8.135", username="eslam", password="eslam", device_type="cisco_ios")
    vxr.enable()
    vxr.config_mode()
    vxr.send_command_timing(R2)
    show = vxr.send_command_timing("do show run")
    print(show)
elif hello == "static" :
    with open("static.yaml") as file3:
        data3 =yaml.full_load(file3)
    from jinja2 import Environment, FileSystemLoader
    env = Environment(loader=FileSystemLoader("."))
    temp = env.get_template("static.j2")
    R3 = temp.render(int=data3)
    vxr = ConnectHandler(host="192.168.8.135", username="eslam", password="eslam", device_type="cisco_ios")
    vxr.enable()
    vxr.config_mode()
    vxr.send_command_timing(R3)
    show = vxr.send_command_timing("do show run")
    print(show)
else:
    print("please write only bpg or ospf or staic only!!!")


