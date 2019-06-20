# -*- coding: utf-8 -*-
# @Author  : Jaywatson
# @File    : threadClass.py
# @Software: PyCharm
import re


class nmon_data_deal:
    def __init__(self):
        self.CPU_For_deal = []
        self.DISKName_For_deal = []
        self.DISKXFER_For_deal = []
        self.MEM_For_deal = []
        self.NET_For_deal = []
        self.net_top_temp = []
        self.network_name = {}
        self.ip = ''
        self.os = ''
        self.simpleNumber = 0

    def file_read(self, path):
        info_Maps = {}
        file = open(path, 'r', encoding='UTF-8')
        line = file.readline()
        while line:
            if 'NET,Network' in line:
                data = re.sub('\n', '', line).split(',')
                self.net_top_temp = data
            if 'DISKBUSY,Disk' in line:
                data = re.sub('\n', '', line).split(',')
                self.DISKName_For_deal = data[2:]
                for temp in self.DISKName_For_deal:
                    info_Maps[temp+'_DISKBUSY'] = []
                info_Maps['DISKXFER'] = []
            if 'CPU_ALL,T' in line:
                data = re.sub('\n', '', line).split(',')
                data_need = [float(data[2]), float(data[3]), float(data[5])]
                self.CPU_For_deal.append(data_need)
            if 'DISKBUSY,T' in line:
                data = re.sub('\n', '', line).split(',')
                for i in range(len(self.DISKName_For_deal)):
                    info_Maps[self.DISKName_For_deal[i]+'_DISKBUSY'].append(float(data[i+2]))
            if 'DISKXFER,T' in line:
                data = re.sub('\n', '', line).split(',')
                temp = 0.0
                for i in range(len(self.DISKName_For_deal)):
                    temp += float(data[i+2])
                info_Maps['DISKXFER'].append(temp)
            if 'MEM,T' in line:
                data = re.sub('\n', '', line).split(',')
                data_need = [float(data[2]), float(data[6]), float(data[-6]), float(data[-3])]
                self.MEM_For_deal.append(data_need)
            if 'NET,T' in line:
                data = re.sub('\n', '', line).split(',')
                data_need = [float(data[self.net_top_temp.index(self.network_name[templine]+'-read-KB/s')]), float(data[self.net_top_temp.index(self.network_name[templine]+'-write-KB/s')])]
                self.NET_For_deal.append(data_need)
            if ',ifconfig,"' in line and self.ip == '':
                if len(re.findall('\,ifconfig\,\"(.+)\s+Link', line)) != 0:
                    tempponit = int(re.sub('\n', '', line).split(',')[1])
                    self.network_name[str(int(tempponit)+1)] = re.findall('\,ifconfig\,\"(.+)\s+Link', line)[0].strip().replace(":0", "")
                if len(re.findall('\,ifconfig\,\"(.+)\:\sflag', line)) != 0:
                    tempponit = int(re.sub('\n', '', line).split(',')[1])
                    self.network_name[str(int(tempponit)+1)] = re.findall('\,ifconfig\,\"(.+)\:\sflag', line)[0].strip().replace(":0", "")
                if len(re.findall('inet\saddr\:((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))\s.+\s\sMask:255.255.255.0', line)) != 0:
                    self.ip = re.findall('inet\saddr\:((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))\s.+\s\sMask:255.255.255.0', line)[0].strip()
                    templine = re.sub('\n', '', line).split(',')[1]
                if len(re.findall('inet\s((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))\s.+netmask\s255.255.255.0', line)) != 0:
                    self.ip = re.findall('inet\s((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))\s.+netmask\s255.255.255.0', line)[0].strip()
                    templine = re.sub('\n', '', line).split(',')[1]
            if 'AAA,snapshots,' in line:
                self.simpleNumber = int(re.findall('AAA,snapshots\,(.+)\n', line)[0].strip())
            if 'AAA,OS,' in line:
                self.os = re.findall('AAA,OS\,(.+)\n', line)[0].strip()
            line = file.readline()
        file.close()
        info_Maps['cpu'] = self.CPU_For_deal
        info_Maps['mem'] = self.MEM_For_deal
        info_Maps['NET'] = self.NET_For_deal
        info_Maps['diskName'] = self.DISKName_For_deal
        info_Maps['network_name'] = self.network_name
        info_Maps['ip'] = self.ip
        info_Maps['simpleNumber'] = self.simpleNumber
        info_Maps['os'] = self.os
        return info_Maps


if __name__ == '__main__':
    test = nmon_data_deal()
    test.file_read('temp/axx.nmon')
