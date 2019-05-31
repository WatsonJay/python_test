import paramiko
import re

hostname = '23.105.214.192'
username = 'root'
password = 'rTZ6nzQKmFfQ'
port = 28676

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=hostname,port=port,username=username,password=password)
stdin, stdout, stderr = ssh.exec_command("top -H -b -d 1 -n 1 ")
filesystem_usage = stdout.readlines()
res = "".join(filesystem_usage)
mem_values = re.findall("", res)
print(filesystem_usage)
ssh.close()