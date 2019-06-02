# -*- coding: utf-8 -*-
# @Author  : Jaywatson
# @File    : monitor_server.py
# @Software: PyCharm
import re

import paramiko

class Monitor_server:

    '''
    创建链接
    hostname, port, username, password,访问linux的ip，端口，用户名以及密码
    '''
    def sshConnect(self, hostname, port, username, password):
        paramiko.util.log_to_file('paramiko_log')
        try:
            # 创建一个SSH客户端client对象
            sshClient = paramiko.SSHClient()
            # 获取客户端host_keys,默认~/.ssh/known_hosts,非默认路径需指定
            sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # 创建SSH连接
            sshClient.connect(hostname, port, username, password)
        except Exception as e:
            print("SSH链接失败：[hostname:%s];[username:%s];[error:%s]" % (hostname, username, e))
            exit()
        return sshClient

    '''
    创建命令执行函数
    command 传入linux运行指令
    '''

    def sshExecCmd(self, sshClient, command):

        stdin, stdout, stderr = sshClient.exec_command(command)
        filesystem_usage = stdout.readlines()
        return filesystem_usage

    '''
    关闭ssh
    '''

    def sshClose(self, sshClient):
        sshClient.close()

    '''内存监控'''

    def get_mem_info(self, sshClient):
        command = 'cat /proc/meminfo'
        get_msgs = self.sshExecCmd(sshClient, command)
        MemTotal = int(re.findall("MemTotal\:\s*(\d+)\skB\n", "".join(get_msgs))[0])
        MemFree = int(re.findall("MemFree\:\s*(\d+)\skB\n", "".join(get_msgs))[0])
        UsedMem = round((MemTotal - MemFree) / MemTotal * 100, 2)
        Buffers = round(int(re.findall("Buffers\:\s*(\d+)\skB\n", "".join(get_msgs))[0]) / MemTotal * 100, 2)
        Cached = round(int(re.findall("Cached\:\s*(\d+)\skB\n", "".join(get_msgs))[0]) / MemTotal * 100, 2)
        SwapCached = round(int(re.findall("SwapCached\:\s*(\d+)\skB\n", "".join(get_msgs))[0]) / MemTotal * 100, 2)
        Mem_info = [UsedMem, Buffers, Cached, SwapCached]
        return Mem_info

    '''磁盘空间监控'''

    def get_disk_stat(self, sshClient):
        command = 'df -h'


    '''端口监控'''

    def get_Com_Str(self, sshClient):
        command = 'netstat -tpln'

    def get_Cpu_info(self, sshClient):
        command = 'top -b -n 1'
        get_msgs = self.sshExecCmd(sshClient, command)
        user_used = float(re.findall("(\d+\.?\d*)\sus\,", "".join(get_msgs))[0])
        sys_used = float(re.findall("(\d+\.?\d*)\ssy\,", "".join(get_msgs))[0])
        free = float(re.findall("(\d+\.?\d*)\sid\,", "".join(get_msgs))[0])
        total_Used = round(100.0 - free, 2)
        cpu_info = [user_used, sys_used, total_Used]
        return cpu_info


if __name__ == '__main__':
    hostname = '192.168.132.129'
    username = 'root'
    password = 'jaywatson'
    port = 22
    moni = Monitor_server()
    test_sshConnect = moni.sshConnect(hostname,port,username,password)
    cpu_info = moni.get_Cpu_info(test_sshConnect)
    Mem_info = moni.get_mem_info(test_sshConnect)
    print(cpu_info)
    print(Mem_info)