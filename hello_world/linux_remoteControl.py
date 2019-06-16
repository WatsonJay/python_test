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
            free = float(re.findall("(\d+\.?\d*)\%id\,", "".join(get_msgs))[0])
            total_Used = round(100.0 - free, 2)
            cpu_info = total_Used
            return cpu_info
        except Exception as e:
            return 0.00
        
    def nmon_checked(self, sshClient):
        try:
            command = 'find ~/monitor -name monitor_used'
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

    def sftp_download_file(self, hostname, port, username, password):
        try:
            t = paramiko.Transport((hostname, port))
            t.connect(username=username, password=password)
            sftp = paramiko.SFTPClient.from_transport(t)
            sftp.get('/home/monitor/axx.nmon', 'temp/axx.nmon', callback=self.callback)
        except Exception as e:
            return e

    '''磁盘空间监控'''

    def nmon_run(self, sshClient):
        try:
            command = '/home/monitor/monitor_used -s 1 -c 120 -F test.nmon  -m /home/monitor/'
            get_msgs = self.sshExecCmd(sshClient, command)
            return get_msgs
        except Exception as e:
            return e

    def callback(self, current, total):
        print("下载了{}".format(round(current/total*100, 2)))

if __name__ == '__main__':
    hostname = '192.168.132.129'
    username = 'root'
    password = 'jaywatson'
    port = 22
    moni = Monitor_server()
    test_sshConnect = moni.sshConnect(hostname,port,username,password)
    cpu_info = moni.get_Cpu_info(test_sshConnect)
    Mem_info = moni.get_mem_info(test_sshConnect)
    disk_info = moni.get_disk_stat(test_sshConnect)
    nmon_checked = moni.nmon_checked(test_sshConnect)
    text = moni.sftp_upload_file(hostname, port, username, password)
    get_msgs = moni.nmon_run(test_sshConnect)
    moni.sftp_download_file(hostname, port, username, password)
    print(cpu_info)
    print(Mem_info)
    print(disk_info)
    print(nmon_checked)
    print(get_msgs)
