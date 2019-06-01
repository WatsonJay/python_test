import paramiko
import re

hostname = '192.168.132.129'
username = 'root'
password = 'jaywatson'
port = 22

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=hostname,port=port,username=username,password=password)
stdin, stdout, stderr = ssh.exec_command("cat /proc/meminfo")
filesystem_usage = stdout.readlines()
MemTotal = int(re.findall("MemTotal\:\s*(\d+)\skB\n","".join(filesystem_usage))[0])
MemFree = int(re.findall("MemFree\:\s*(\d+)\skB\n","".join(filesystem_usage))[0])
UsedMem = round((MemTotal - MemFree) / MemTotal * 100, 2)
Buffers = round(int(re.findall("Buffers\:\s*(\d+)\skB\n","".join(filesystem_usage))[0])/ MemTotal * 100, 2)
Cached = round(int(re.findall("Cached\:\s*(\d+)\skB\n","".join(filesystem_usage))[0])/ MemTotal * 100, 2)
SwapCached = round(int(re.findall("SwapCached\:\s*(\d+)\skB\n","".join(filesystem_usage))[0])/ MemTotal * 100, 2)
Mem_info = [UsedMem, Buffers, Cached, SwapCached]
print(Mem_info)
ssh.close()