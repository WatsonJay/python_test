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
    def fild_data_by_row(self, sheetName="",startRow=0,startCol=0,dataMap={},datas=[],title=False):
        dataArea = {}
        dataArea['data_type'] = 'by_row'
        dataArea['data_keys'] = []
        if sheetName != "":
            currentSheet = self.workBook.get_worksheet_by_name(sheetName)
            if currentSheet == None:
                currentSheet = self.workBook.add_worksheet(sheetName)
            dataArea['title'] = title
            tmpRow = startRow
            col_width = {}
            if title:
                col = startCol
                for key in dataMap.keys():
                    currentSheet.write_string(tmpRow, col, str(key).title(), self.title_format)
                    col_width[col] = len_byte(str(key))
                    col += 1
                tmpRow += 1
            index = 0
            line_format = self.workBook.add_format({'align': 'center'})
            for data in datas:
                col = startCol
                for key,value in dataMap.items():
                    temp_val = None
                    if key not in dataArea['data_keys']:
                        dataArea['data_keys'].append(key)
                    if value == 'index':
                        temp_val = str(index)
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
                        temp_val = data[dataKey]
                        currentSheet.write(tmpRow, col, temp_val)
                    if len_byte(str(temp_val)) > col_width[col]:
                        col_width[col] = len_byte(str(temp_val))
                    col += 1
                index += 1
                tmpRow += 1
            if (title):
                currentSheet.freeze_panes(startRow + 1, 0, tmpRow, 0)
            dataArea['area'] = (startRow,tmpRow,startCol,col)
            for key,value in col_width.items():
                currentSheet.set_column(key, key, value+2)
            return dataArea

    '''以列填充数据项填充数据项'''
    def fild_data_by_col(self,sheetName="",startRow=0,startCol=0,dataMap={},datas=[],title=False):
        dataArea = {}
        dataArea['data_type'] = 'by_col'
        dataArea['data_keys'] = []
        if sheetName != "":
            currentSheet = self.workBook.get_worksheet_by_name(sheetName)
            if currentSheet == None:
                currentSheet = self.workBook.add_worksheet(sheetName)
            dataArea['title'] = title
            tmpCol = startCol
            col_width = {}
            col_width[tmpCol] = 0
            if title:
                row = startRow
                currentSheet.freeze_panes(startRow+1, 0)
                for key in dataMap.keys():
                    currentSheet.write_string(row, tmpCol, key, self.title_format)
                    if col_width[tmpCol] < len_byte(str(key)):
                        col_width[tmpCol] = len_byte(str(key))
                    row += 1
                tmpCol += 1
                col_width[tmpCol] = 0
            index = 1
            line_format = self.workBook.add_format({'align': 'center'})
            for data in datas:
                row = startRow
                for key,value in dataMap.items():
                    temp_val = None
                    if key not in dataArea['data_keys']:
                        dataArea['data_keys'].append(key)
                    if value == 'index':
                        temp_val = str(index)
                        currentSheet.write_string(row, tmpCol, temp_val, line_format)
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
                        temp_val = data[dataKey]
                        currentSheet.write(row, tmpCol, temp_val)
                    if len_byte(str(temp_val)) > col_width[tmpCol]:
                        col_width[tmpCol] = len_byte(str(temp_val))
                    row += 1
                index += 1
                tmpCol += 1
                col_width[tmpCol] = 0
            if (title):
                currentSheet.freeze_panes(startRow + 1, 0, row, 0)
            dataArea['area'] = (startRow, row, startCol, tmpCol)
            for key,value in col_width.items():
                currentSheet.set_column(key, key, value+2)
            return dataArea

    '''填充数据图表'''
    def fild_simple_chart(self,sheetName="",dataArea={},seriesMap=[],categorie='',place=(0,0)):
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
                        chart_width = rows[1] - rows[0]
                        if categorie_index != -1:
                            tmp_serie['categories'] = [sheetName, rows[0], categorie_index, rows[1], categorie_index]
                    elif dataArea['data_type'] == 'by_col':
                        if dataArea['title']:
                            cols = (tmp_area[2] + 1, tmp_area[3] - 1)
                            tmp_serie['name'] = [sheetName, index, tmp_area[2]]
                        else:
                            cols = (tmp_area[2], tmp_area[3] - 1)
                        tmp_serie['values'] = [sheetName, index, cols[0], index, cols[1]]
                        chart_width = cols[1] - cols[0]
                        if categorie_index != -1:
                            tmp_serie['categories'] = [sheetName, categorie_index, cols[0], categorie_index, cols[1]]
                    else:
                        raise Exception
                    temp_chart.add_series(tmp_serie)
                    if chart_width < 700:
                        chart_width = 700
                    temp_chart.set_size({'width': chart_width , 'height': 500})
                for value in charts.values():
                    if chart == None:
                        chart = value
                    else:
                        chart.combine(value)
        currentSheet.set_selection(place[0], place[1], place[0], place[1])
        currentSheet.insert_chart(place[0], place[1], chart)

    '''以行填充数据结果'''
    def fild_sum_by_row(self):
        print(1)

    '''以列填充数据结果'''
    def fild_sum_by_col(self):
        print(1)

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


