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
        paramiko.util.log_to_file('paramiko_log')
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
        mem_info = {"memTotal": 0, "memFree": 0, "memUsed": 0}
        try:
            command = 'cat /proc/meminfo'
            get_msgs = self.sshExecCmd(sshClient, command)
            MemTotal = int(re.findall("MemTotal\:\s*(\d+)\skB\n", "".join(get_msgs))[0])
            MemFree = int(re.findall("MemFree\:\s*(\d+)\skB\n", "".join(get_msgs))[0])
            Cached = int(re.findall("Cached\:\s*(\d+)\skB\n", "".join(get_msgs))[0])
            Buffers = int(re.findall("Buffers\:\s*(\d+)\skB\n", "".join(get_msgs))[0])
            UsedMem = int(MemTotal - MemFree - Cached - Buffers)
            mem_info = {"memTotal": MemTotal, "memFree": MemFree, "memUsed": UsedMem}
        except Exception as e:
            pass
        finally:
            return mem_info

    '''磁盘空间监控'''
    def get_disk_stat(self, sshClient):
        disk_info = {"diskTotal": 0, "diskFree": 0, "diskUsed": 0}
        try:
            command = 'df -h ~'
            get_msgs = self.sshExecCmd(sshClient, command)
            disk_temp = re.findall("(\d+\.?\d*)", "".join(get_msgs))
            disk_free = float(disk_temp[2])
            disk_total = float(disk_temp[0])
            disk_used = float(disk_temp[1])
            disk_info = {"diskTotal": disk_total, "diskFree": disk_free, "diskUsed": disk_used}
        except Exception as e:
            pass
        finally:
            return disk_info

    '''Cpu监控'''
    def get_Cpu_info(self, sshClient):
        cpu_info = {"cpuSys": 0, "cpuFree": 0, "cpuUsed": 0}
        try:
            command = 'top -b -n 1'
            get_msgs = self.sshExecCmd(sshClient, command)
            try:
                free = float(re.findall("(\d+\.?\d*)\%id\,", "".join(get_msgs))[0])
                sys = float(re.findall("(\d+\.?\d*)\%sy\,", "".join(get_msgs))[0])
                used = float(re.findall("(\d+\.?\d*)\%us\,", "".join(get_msgs))[0])
            except Exception as e:
                free = float(re.findall("(\d+\.?\d*)\sid\,", "".join(get_msgs))[0])
                sys = float(re.findall("(\d+\.?\d*)\ssy\,", "".join(get_msgs))[0])
                used = float(re.findall("(\d+\.?\d*)\sus\,", "".join(get_msgs))[0])
            cpu_info = {"cpuSys": sys, "cpuFree": free, "cpuUsed": used}
        except Exception as e:
            pass
        finally:
            return cpu_info


if __name__ == '__main__':
    client = Monitor_server()
    sshClient = client.sshConnect('192.168.174.128',22,'root','123456')
    mem = client.get_mem_info(sshClient)
    disk = client.get_disk_stat(sshClient)
    cpu = client.get_Cpu_info(sshClient)
    client.sshClose(sshClient)
