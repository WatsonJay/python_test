# -*- coding: utf-8 -*-
__author__ = 'Jaywatson'

import configparser

class config:

    # 读取配置文件
    def readConfig(self):
        config = configparser.ConfigParser()
        config.read("config/config.ini", encoding="utf-8")
        return config

    # 写入配置文件
    def writeConfig(self,config):
        config.write(open("config/config.ini", "w", encoding='utf-8'))

    # 新增section
    def addSection(self, section):
        config = self.readConfig()
        if not config.has_section(section):  # 检查是否存在section
            config.add_section(section)
        self.writeConfig(config)

    # 新增option
    def addoption(self, section, option, word):
        config = self.readConfig()
        config.set(section, option, word)
        self.writeConfig(config)

    # 删除配置文件
    def delSection(self, section):
        config = self.readConfig()
        if config.has_section(section):
            config.remove_section(section)  # 整个section下的所有内容都将删除
        self.writeConfig(config)

    #获得配置
    def getOption(self, section, option):
        config = self.readConfig()
        if config.has_section(section):
            word = config.get(section, option)
        else :
            word = ''
        return word

    # 获得配置
    def getSection(self):
        config = self.readConfig()
        word = config.sections()
        if 'qun' in word:
            word.remove('qun')
        return word


    # 字符串切割成数组
    def splitword(self,word):
        if word != '':
            list = word.split(',')
        else:
            list = []
        return list

    # 数组转成字符串
    def split(self, list):
        if len(list) > 0:
            word = ','.join(list)
        else:
            word = ''
        return word