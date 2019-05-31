# -*- coding: utf-8 -*-
# @Author  : Jaywatson
# @File    : monitor_server.py
# @Software: PyCharm

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

    def mem_info(self, linuxInfo):
        command = 'cat /proc/meminfo'

    '''磁盘空间监控'''

    def disk_stat(self, linuxInfo):
        command = 'df -h'

    '''端口监控'''

    def get_Com_Str(self, linuxInfo):
        command = 'netstat -tpln'

