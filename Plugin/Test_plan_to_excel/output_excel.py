import os
from xlrd import open_workbook
import xlwt,xlrd

# -*- coding: utf-8 -*-
class Print_out_misson_value(object):
#未完成
    def __init__(self, inf):
        self.inf = inf

    def read_excel_to_misson_value():
        pass

    def read_txt():
        pass

    def plan_excel(self):
        print(self.inf + "/test1")

    def finish_excel(self):
        print(self.inf + "/test2")


class Print_out_misson_project(object):
    def __init__(self, inf):
        self.inf = inf
    
    def read_excel(self,path):
        worksheet = xlrd.open_workbook(path)   #打开excel文件
        sheet_names= worksheet.sheet_names()    #获取excel中所有工作表名
        # print(sheet_names)
        target_sheet = worksheet.sheet_by_name('委托项')
        rows = target_sheet.col_values(0)
        del rows[0]
        # print(rows)
        return rows
    # if __name__ == '__main__':
    #     # read_excel('D:\MyData\pengjw3\Downloads\pengjw3_1569045729044.xls')
        #     pass

    def plan_excel(self):
        print(self.inf + "/test1")

    def finish_excel(self):
        print(self.inf + "/test2")

class Find_file(object):
    def __init__(self, inf):
        self.inf = inf

    def findfile(self,file_value,file_path,file_name = ""):
        filelists = []
        filelist = os.listdir(file_path)
        for filename in filelist:
            if file_value in filename:
                if file_name != "":
                    if file_name in filename:
                        filelists.append(file_path+'\\'+filename)
                else:
                    filelists.append(file_path+'\\'+filename)
        return filelists

class Change_Excel(object):
    def __init__(self, inf):
        self.inf = inf

    def read_excel(self,path):
        worksheet = xlrd.open_workbook(path)   #打开excel文件
        sheet_names= worksheet.sheet_names()    #获取excel中所有工作表名
        # print(sheet_names)
        target_sheet = worksheet.sheet_by_name('净饮产品APP功能测试用例')
        rows = target_sheet.col_values(2)
        rows.remove(rows[0])
        print(rows)
        # return rows

    def change_to_zentao(self, path):
        self.value = value

# from xlrd import open_workbook
# import xlwt,xlrd,csv
# Change_Excel('none').read_excel(r'D:\MyData\pengjw3\Downloads\美居5.6厨热APP测试用例-（JR1959S-NF：FT1：63100FT1）.xlsx')
        



class Teach_How_To_Use(object):
    def __init__(self, inf):
        self.inf = inf

    def print_value(self, path):
        self.value = path
        # 属性设置
        print(self.value + self.inf + path)

#用法
# Teach_How_To_Use("b").print_value("test") 