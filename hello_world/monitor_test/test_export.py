# -*- coding: utf-8 -*-
# @Time    : 2020/7/1 17:15
# @Author  : Jaywatson
# @File    : test_export.py
# @Soft    : python_test
from hello_world.monitor_test.excel_export import Excel
from hello_world.monitor_test.nmon_analysis import nmon_analysis

if __name__ == "__main__":
    test = nmon_analysis()
    test.file_analysis('temp/axx.nmon')
    nmon_data = test.analysis
    dataMap = {}
    for item in nmon_data['dataItems']['CPU_ALL']:
        dataMap[item] = "{" + item + "}"
    dataMap['free%'] = 'SUM: 100-{User%}-{Sys%}'
    execl = Excel("test")
    dataArea = execl.fild_data_by_row("test1", 0, 0, dataMap, nmon_data['CPU_ALL'], True)
    seriesMap = [{'type': 'column', 'key': 'User%'}, {'type': 'column', 'key': 'Sys%'}]
    execl.fild_simple_chart("test1", dataArea, seriesMap,'time')
    execl.save_workBook()