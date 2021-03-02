from netmiko import ConnectHandler
from getpass import getpass
import datetime

"""
    Fortinet consoles configuration and save it to the local path
    :param username: string for username with access
    :param password: string for password
"""

current_time = datetime.datetime.today().strftime('%d-%b-%y_%H-%M-%S')

def switch():
    print("\n1: Backup configuracao da FortiManager")
    print("2: Backup configuracao da FortiGate")
    print("3: Backup configuracao da FortiAnalyser")
    print("4: Backup configuracao da FortiEMS")
    print("5: Backup configuracao da FortiMail")
    print("6: Backup configuracao da FortiAuthenticator")
    print("7: Backup configuracao da FortiWeb")
    print("8: Backup configuracao da FortiADC\n")
    
    option = int(input("Selecione uma opcao: "))
    
    if option == 1:
        
        username = input("Introduzir utilizador: ")
        password = getpass("Introduza a password: ")
        
        ip = '< introduzir ip >'
        
        my_config = {
                'device_type': 'fortinet',
                'ip': ip,
                'username': username,
                'password': password
            }
        
        net_connect = ConnectHandler(**my_config)
        
        outputFortiManager = net_connect.send_command('show')
        
        with open('FortiManager_Backup' + '_' + current_time + '.cfg', "w") as file :
    
            for line in outputFortiManager:
                file.write(line)
        close()
                
        return file
 
    elif option == 2:

        username = input("Introduzir utilizador: ")
        password = getpass("Introduza a password: ")
    
        ip = '< introduzir ip >'
        
        my_config = {
                'device_type': 'fortinet',
                'ip': ip,
                'username': username,
                'password': password
            }
        
        net_connect = ConnectHandler(**my_config)
        
        outputFortiGate = net_connect.send_command('show full-configuration')
        
        with open('FortiGate_Backup' + '_' + current_time + '.cfg', "w") as file :
    
            for line in outputFortiGate:
                file.write(line)
        
        close()
        
        return file
    
    elif option == 3:

        username = input("Introduzir utilizador: ")
        password = getpass("Introduza a password: ")
    
        ip = '< introduzir ip >'
        
        my_config = {
                'device_type': 'fortinet',
                'ip': ip,
                'username': username,
                'password': password
            }
        
        net_connect = ConnectHandler(**my_config)
        
        outputFortiAnalyser = net_connect.send_command('show')
        
        with open('FortiAnalyser_Backup' + '_' + current_time + '.cfg', "w") as file :
    
            for line in outputFortiAnalyser:
                file.write(line)
        
        close()
            
        return file

    elif option == 4:

        username = input("Introduzir utilizador: ")
        password = getpass("Introduza a password: ")
    
        ip = '< introduzir ip >'
        
        my_config = {
                'device_type': 'fortinet',
                'ip': ip,
                'username': username,
                'password': password
            }
        
        net_connect = ConnectHandler(**my_config)
        
        outputFortiEMS = net_connect.send_command('show full-configuration')
        
        with open('FortiEMS_Backup' + '_' + current_time + '.cfg', "w") as file :
    
            for line in outputFortiEMS:
                file.write(line)
            
        close()
        
        return file    

    elif option == 5:

        username = input("Introduzir utilizador: ")
        password = getpass("Introduza a password: ")
    
        ip = '< introduzir ip >'
        
        my_config = {
                'device_type': 'fortinet',
                'ip': ip,
                'username': username,
                'password': password
            }
        
        net_connect = ConnectHandler(**my_config)
        
        outputFortiMail = net_connect.send_command('show full-configuration')
        
        with open('FortiMail_Backup' + '_' + current_time + '.cfg', "w") as file :
    
            for line in outputFortiMail:
                file.write(line)
        
        close()
            
        return file

    elif option == 6:

        username = input("Introduzir utilizador: ")
        password = getpass("Introduza a password: ")
    
        ip = '< introduzir ip >'
        
        my_config = {
                'device_type': 'fortinet',
                'ip': ip,
                'username': username,
                'password': password
            }
        
        net_connect = ConnectHandler(**my_config)
        
        outputFortiAuthenticator = net_connect.send_command('show full-configuration')
        
        with open('FortiAuthenticator_Backup' + '_' + current_time + '.cfg', "w") as file :
    
            for line in outputFortiAuthenticator:
                file.write(line)
        
        close()
            
        return file           

    elif option == 7:

        username = input("Introduzir utilizador: ")
        password = getpass("Introduza a password: ")
    
        ip = '< introduzir ip >'
        
        my_config = {
                'device_type': 'fortinet',
                'ip': ip,
                'username': username,
                'password': password
            }
        
        net_connect = ConnectHandler(**my_config)
        
        outputFortiWeb = net_connect.send_command('show full-configuration')
        
        with open('FortiWeb_Backup' + '_' + current_time + '.cfg', "w") as file :
    
            for line in outputFortiWeb:
                file.write(line)
        
        close()
            
        return file

    elif option == 8:

        username = input("Introduzir utilizador: ")
        password = getpass("Introduza a password: ")
    
        ip = '< introduzir ip >'
        
        my_config = {
                'device_type': 'fortinet',
                'ip': ip,
                'username': username,
                'password': password
            }
        
        net_connect = ConnectHandler(**my_config)
        
        outputFortiADC = net_connect.send_command('show full-configuration')
        
        with open('FortiADC_Backup' + '_' + current_time + '.cfg', "w") as file :
    
            for line in outputFortiADC:
                file.write(line)
        
        close()
        
        return file

    else:
        print("Incorrect option")
 
switch()

