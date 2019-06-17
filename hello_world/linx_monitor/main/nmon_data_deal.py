# -*- coding: utf-8 -*-
# @Author  : Jaywatson
# @File    : threadClass.py
# @Software: PyCharm
import re

class nmon_data_deal:
    def __init__(self):
        self.CPU_For_deal = []
        self.DISKBUSY_For_deal = []
        self.DISKXFER_For_deal = []
        self.MEM_For_deal = []
        self.NET_For_deal = []
        self.network_name = ''
        self.ip = ''
        self.os = ''
        self.simpleNumber = 0

    def file_read(self ,path):
        file = open(path, 'r', encoding='UTF-8')
        line = file.readline()
        while line:
            if 'CPU_ALL,T' in line:
                data = re.sub('\n', '', line).split(',')
                data_need = [data[2],data[3],data[5]]
                self.CPU_For_deal.append(data_need)
            if 'DISKBUSY,T' in line:
                data = re.sub('\n', '', line).split(',')
                data_need = [ data[-6], data[-5], data[-4], data[-3], data[-2], data[-1]]
                self.DISKBUSY_For_deal.append(data_need)
            if 'DISKXFER,T' in line:
                data = re.sub('\n', '', line).split(',')
                data_need = [data[-6], data[-5], data[-4], data[-3], data[-2], data[-1]]
                self.DISKXFER_For_deal.append(data_need)
            if 'MEM,T' in line:
                data = re.sub('\n', '', line).split(',')
                data_need = [data[2], data[6], data[-6], data[-3]]
                self.MEM_For_deal.append(data_need)
            if 'NET,T' in line:
                data = re.sub('\n', '', line).split(',')
                data_need = [data[3], data[-2]]
                self.NET_For_deal.append(data_need)
            if ',ifconfig,"' in line and self.ip == '':
                if len(re.findall('\,ifconfig\,\"(.+)\s\s\s\s\s\sLink', line)) != 0:
                    self.network_name = re.findall('\,ifconfig\,\"(.+)\s\s\s\s\s\sLink', line)[0].strip()
                if len(re.findall('\,ifconfig\,\"(.+)\:\s', line)) != 0:
                    self.network_name = re.findall('\,ifconfig\,\"(.+)\:\s', line)[0].strip()
                if len(re.findall('inet\saddr\:(.+)\sBcast\:', line)) != 0:
                    self.ip = re.findall('inet\saddr\:(.+)\sBcast\:', line)[0].strip()
                if len(re.findall('inet\s(.+)\s\snetmask', line)) != 0:
                    self.ip = re.findall('inet\s(.+)\s\snetmask', line)[0].strip()
            if 'AAA,snapshots,' in line:
                self.simpleNumber = int(re.findall('AAA,snapshots\,(.+)\n', line)[0].strip())
            if 'AAA,OS,' in line:
                self.os = re.findall('AAA,OS\,(.+)\n', line)[0].strip()
            line = file.readline()
        file.close()
        info_Maps = {}
        info_Maps['cpu'] = self.CPU_For_deal
        info_Maps['diskBusy'] = self.DISKBUSY_For_deal
        info_Maps['diskXfer'] = self.DISKXFER_For_deal
        info_Maps['mem'] = self.MEM_For_deal
        info_Maps['NET'] = self.NET_For_deal
        info_Maps['network_name'] = self.network_name
        info_Maps['ip'] = self.ip
        info_Maps['simpleNumber'] = self.simpleNumber
        info_Maps['os'] = self.os
        return info_Maps

if __name__ == '__main__':
    test = nmon_data_deal()
    test.file_read('temp/axx.nmon')