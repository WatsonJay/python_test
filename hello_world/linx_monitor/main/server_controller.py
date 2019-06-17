# -*- coding: utf-8 -*-
# @Author  : Jaywatson
# @File    : server_controller.py
# @Software: PyCharm
import re
import paramiko

class Monitor_server:
    '''
    创建链接
    hostname, port, username, password,访问linux的ip，端口，用户名以及密码
    '''
    def sshConnect(self, hostname, port, username, password):
        paramiko.util.log_to_file('log/paramiko_log')
        # 创建一个SSH客户端client对象
        sshClient = paramiko.SSHClient()
        # 获取客户端host_keys,默认~/.ssh/known_hosts,非默认路径需指定
        sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 创建SSH连接
        sshClient.connect(hostname, port, username, password)
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
        try:
            command = 'cat /proc/meminfo'
            get_msgs = self.sshExecCmd(sshClient, command)
            MemTotal = int(re.findall("MemTotal\:\s*(\d+)\skB\n", "".join(get_msgs))[0])
            MemFree = int(re.findall("MemFree\:\s*(\d+)\skB\n", "".join(get_msgs))[0])
            UsedMem = round((MemTotal - MemFree) / MemTotal * 100, 2)
            Mem_info = UsedMem
            return Mem_info
        except Exception as e:
            return 0.00

    '''磁盘空间监控'''
    def get_disk_stat(self, sshClient):
        try:
            command = 'df -h ~'
            get_msgs = self.sshExecCmd(sshClient, command)
            disk_free = float(re.findall("(\d+\.?\d*)\%", "".join(get_msgs))[0])
            return disk_free
        except Exception as e:
            return 0.00

    '''Cpu监控'''
    def get_Cpu_info(self, sshClient):
        try:
            command = 'top -b -n 1'
            get_msgs = self.sshExecCmd(sshClient, command)
            try:
                free = float(re.findall("(\d+\.?\d*)\%id\,", "".join(get_msgs))[0])
            except Exception as e:
                free = float(re.findall("(\d+\.?\d*)\sid\,", "".join(get_msgs))[0])
            total_Used = round(100.0 - free, 2)
            cpu_info = total_Used
            return cpu_info
        except Exception as e:
            return 0.00

    '''运行nmon'''
    def nmon_run(self, sshClient, name, time, tap):
        try:
            command = '/home/monitor/monitor_used -s '+time+' -c '+tap+' -F '+name+'.nmon  -m /home/monitor/'
            get_msgs = self.sshExecCmd(sshClient, command)
            if get_msgs == []:
                return '启动运行,请稍后'
            else:
                return get_msgs
        except Exception as e:
            return e

    def nmon_checked(self, sshClient):
        try:
            command = 'find /home/monitor -name monitor_used'
            get_msgs = self.sshExecCmd(sshClient, command)
            if len(re.findall("/monitor/monitor_used", "".join(get_msgs))) > 0:
                return True
            else:
                return False
        except Exception as e:
            return False

    def sftp_upload_file(self,hostname,port,username,password):
        try:
            t = paramiko.Transport((hostname, port))
            t.connect(username=username, password=password)
            sftp = paramiko.SFTPClient.from_transport(t)
            try:
                sftp.stat('/home/monitor/')
            except IOError:
                sftp.mkdir('/home/monitor/', 0o777)
            sftp.put('temp/monitor_used','/home/monitor/monitor_used')
            sftp.chmod('/home/monitor/monitor_used', 0o777)
            t.close()
            return '上传成功'
        except Exception as e:
            return e