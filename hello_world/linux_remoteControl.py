import paramiko
import re

hostname = '192.168.132.129'
username = 'root'
password = 'jaywatson'
port = 22

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=hostname,port=port,username=username,password=password)
stdin, stdout, stderr = ssh.exec_command("df")
filesystem_usage = stdout.readlines()
print("".join(filesystem_usage))
ssh.close()