# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 11:10
# @Author  : Jaywatson
# @File    : nmon_analysis.py
# @Soft    : python_test
import re
from datetime import datetime

class nmon_analysis:
    def __init__(self):
        self.analysis = {}

    def file_analysis(self, path):
        try:
            dataType = ["AAA","BBBP","ZZZZ"]
            self.analysis["dataTypeList"] = dataType
            self.analysis["ZZZZ"] = {}
            self.analysis["AAA"] = {}
            self.analysis["BBBP"] = {}
            self.analysis["dataItems"] = {}
            with open(path, 'r', encoding='UTF-8') as f:
                for line in f:
                    if line.startswith("AAA"):
                        self.AAA_analysis(line)
                    elif line.startswith("BBBP"):
                        self.BBBP_analysis(line)
                    elif line.startswith("ZZZZ"):
                        self.ZZZZ_analysis(line)
                    else:
                        self.DATA_analysis(line)
                del self.analysis["ZZZZ"]
        except Exception as e:
            print(line + str(e))

    def AAA_analysis(self,line):
        datas = re.sub('\n', '', line).split(',')
        if len(datas) > 0 and len(datas) == 3:
            self.analysis["AAA"][datas[1]] = datas[-1]

    def BBBP_analysis(self,line):
        datas = re.sub('\n', '', line).split(',')
        if len(datas) > 0 and len(datas) == 4:
            if datas[2] not in self.analysis["BBBP"]:
                self.analysis["BBBP"][datas[2]] = datas[-1].strip('"')
            else:
                self.analysis["BBBP"][datas[2]] += ("\n" + datas[-1].strip('"'))

    def ZZZZ_analysis(self,line):
        datas = re.sub('\n', '', line).split(',')
        if len(datas) > 0:
            date = datetime.strftime(datetime.strptime(datas[-1] + " " +datas[-2], '%d-%b-%Y %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
            self.analysis["ZZZZ"][datas[1]] = date

    def DATA_analysis(self,line):
        datas = re.sub('\n', '', line).split(',')
        if len(datas) > 0:
            if datas[0] not in self.analysis["dataTypeList"]:
                self.analysis["dataTypeList"].append(datas[0])
                self.analysis[datas[0]] = []
                temp_list = ['time']
                for data in datas[2:]:
                    temp_list.append(data)
                self.analysis["dataItems"][datas[0]] = temp_list
            else:
                temp_map = {}
                for i in range(len(datas)-2):
                    key = self.analysis["dataItems"][datas[0]][i+1]
                    temp_map[key] = self.str_float(datas[i+2])
                datetime = self.analysis["ZZZZ"][datas[1]]
                temp_map['time'] = datetime
                self.analysis[datas[0]].append(temp_map)

    def str_float(self,data):
        try:
            return float(data)
        except:
            return data