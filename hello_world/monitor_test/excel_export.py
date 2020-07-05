# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 19:19
# @Author  : Jaywatson
# @File    : execl_export.py
# @Soft    : python_test
import re

import xlsxwriter
from hello_world.monitor_test.excel_util import *

class Excel:

    def __init__(self,name=""):
        self.workBook = xlsxwriter.Workbook(name+".xlsx")
        self.title_format = self.workBook.add_format({'bold': True, 'align': 'center'})

    '''以行填充数据项填充数据项'''
    def fild_data_by_row(self, sheetName="", startRow=0, startCol=0, dataMap = {}, datas=[], title=False):
        dataArea = {}
        dataArea['data_type'] = 'by_row'
        dataArea['data_keys'] = []
        if sheetName != "":
            currentSheet = self.workBook.get_worksheet_by_name(sheetName)
            if currentSheet == None:
                currentSheet = self.workBook.add_worksheet(sheetName)
            dataArea['title'] = title
            tmpRow = startRow
            if title:
                col = startCol
                for key in dataMap.keys():
                    currentSheet.write_string(tmpRow, col, key, self.title_format)
                    col += 1
                tmpRow += 1
            index = 0
            line_format = self.workBook.add_format({'align': 'center'})
            for data in datas:
                col = startCol
                for key,value in dataMap.items():
                    if key not in dataArea['data_keys']:
                        dataArea['data_keys'].append(key)
                    if value == 'index':
                        currentSheet.write_string(tmpRow, col, str(index), line_format)
                    elif value.startswith("SUM: "):
                        tmp_cal = value[5:]
                        tmp_cal = tmp_cal.format(**data)
                        try:
                            tmp_val = eval(tmp_cal)
                        except:
                            tmp_val = 0
                        currentSheet.write(tmpRow, col, tmp_val)
                    else:
                        dataKey = re.findall('{(.+)}', value)[0]
                        currentSheet.write(tmpRow, col, data[dataKey])
                    col += 1
                index += 1
                tmpRow += 1
            dataArea['area'] = (startRow,tmpRow,startCol,col)
            return dataArea

    '''以列填充数据项填充数据项'''
    def fild_data_by_col(self, sheetName="", startRow=0, startCol=0, dataMap={}, datas=[], title=False):
        dataArea = {}
        dataArea['data_type'] = 'by_col'
        dataArea['data_keys'] = []
        if sheetName != "":
            currentSheet = self.workBook.get_worksheet_by_name(sheetName)
            if currentSheet == None:
                currentSheet = self.workBook.add_worksheet(sheetName)
            dataArea['title'] = title
            tmpCol = startCol
            if title:
                row = startRow
                for key in dataMap.keys():
                    currentSheet.write_string(row, tmpCol, key, self.title_format)
                    row += 1
                tmpCol += 1
            index = 1
            line_format = self.workBook.add_format({'align': 'center'})
            for data in datas:
                row = startRow
                for key,value in dataMap.items():
                    if key not in dataArea['data_keys']:
                        dataArea['data_keys'].append(key)
                    if value == 'index':
                        currentSheet.write_string(row, tmpCol, str(index), line_format)
                    elif value.startswith("SUM: "):
                        tmp_cal = value[5:]
                        tmp_cal = tmp_cal.format(**data)
                        try:
                            tmp_val = eval(tmp_cal)
                        except:
                            tmp_val = 0
                        currentSheet.write(row, tmpCol, tmp_val)
                    else:
                        dataKey = re.findall('{(.+)}', value)[0]
                        currentSheet.write(row, tmpCol, data[dataKey])
                    row += 1
                index += 1
                tmpCol += 1
            dataArea['area'] = (startRow, row, startCol, tmpCol)
            return dataArea

    '''填充数据项'''
    def fild_simple_chart(self, sheetName="", dataArea={}, seriesMap=[], categorie=''):
        if sheetName != "":
            currentSheet = self.workBook.get_worksheet_by_name(sheetName)
            if len(seriesMap) > 0:
                chart = None
                charts = {}
                tmp_area = dataArea['area']
                for serieMap in seriesMap:
                    if serieMap['type'] not in charts.keys():
                        temp_chart = self.workBook.add_chart({'type': serieMap['type']})
                        charts[serieMap['type']] = temp_chart
                    else:
                        temp_chart = charts[serieMap['type']]
                    tmp_serie = {}
                    index = dataArea['data_keys'].index(serieMap['key'])
                    categorie_index = -1
                    if categorie != '':
                        categorie_index = dataArea['data_keys'].index(categorie)
                    if dataArea['data_type'] == 'by_row':
                        if dataArea['title']:
                            rows = (tmp_area[0] + 1, tmp_area[1] - 1)
                            tmp_serie['name'] = [sheetName, tmp_area[0], index]
                        else:
                            rows = (tmp_area[0], tmp_area[1] - 1)
                        tmp_serie['values'] = [sheetName, rows[0], index, rows[1], index]
                        if categorie_index != -1:
                            tmp_serie['categories'] = [sheetName, rows[0], categorie_index, rows[1], categorie_index]
                    elif dataArea['data_type'] == 'by_col':
                        if dataArea['title']:
                            cols = (tmp_area[2] + 1, tmp_area[3] - 1)
                            tmp_serie['name'] = [sheetName, index, tmp_area[2]]
                        else:
                            cols = (tmp_area[2], tmp_area[3] - 1)
                        tmp_serie['values'] = [sheetName, index, cols[0], index, cols[1]]
                        if categorie_index != -1:
                            tmp_serie['categories'] = [sheetName, categorie_index, cols[0], categorie_index, cols[1]]
                    else:
                        raise Exception
                    temp_chart.add_series(tmp_serie)
                for value in charts.values():
                    if chart == None:
                        chart = value
                    else:
                        chart.combine(value)
        currentSheet.insert_chart('A17', chart)

    '''保存execl'''
    def save_workBook(self):
        try:
            self.workBook.close()
        except xlsxwriter.exceptions.FileCreateError as e:
            pass

if __name__ == "__main__":
    execl = Excel("test")
    dataMap = {'序号': 'index','第一': '{test1}','second': '{test2}', '平均值': 'SUM: avg([{test1}, {test2}])'}
    data = [
        {'test1': 1,'test2': 7},
        {'test1': 2, 'test2': 6},
        {'test1': 3, 'test2': 5},
        {'test1': 4, 'test2': 4},
        {'test1': 5, 'test2': 3},
        {'test1': 6, 'test2': 2},
        {'test1': 7, 'test2': 1}
    ]
    dataArea = execl.fild_data_by_col("test1",0,0,dataMap,data,False)
    startRow = dataArea['area'][1]
    # dataArea2 = execl.fild_data_by_row("test1", startRow + 2, 0, dataMap, data, True)
    execl.fild_simple_chart("test1",dataArea,[{'type':'column','key':'第一'},{'type':'column','key':'second'}],'序号')
    execl.save_workBook()


