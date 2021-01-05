#引入库
import xlwings as xw
import json
import os

from os import path
file_path = path.dirname(__file__)
file_father_path = os.path.dirname(file_path)

import setting

# -*- coding: utf-8 -*-
class Create_xlsl_by_test_inf(object):
#未完成
    def __init__(self,path,inf):
        def check_app_value(inf):
            app_list = setting.global_inf('global_target_app_list')
            for app_value in app_list:
                if(str(app_value) in str(inf['样品名称'])):
                    inf_sample_name = inf['样品名称']
                    break
                else:
                    inf_sample_name = inf['样品名称']+"_"+inf['样品型号']    
                    break
            return inf_sample_name
        
        self.path = path
        self.inf = inf
        self.wb_path = file_path+'\\'
        self.inf_sample_name = check_app_value(self.inf)

    def plan_excel(self,file_name = 'test_plan.xlsx'):
        value_list = []
        inf = self.inf 
        app = xw.App(visible=False,add_book=False)
        save_file_path = self.path+'/'+inf['编码']+'_计划表.xlsx'
        if(os.path.exists(save_file_path)):
            wb = app.books.open(save_file_path)
            sht = wb.sheets[0]        
            value_list = sht.range('a2:v2').value
            value_list[3] = inf['报告日期']
            value_list[9] = inf['样品生产单位']
            value_list[10] = inf['样品编码']
            value_list[11] = inf['检测类别']
            value_list[12] = inf['委托人']
            value_list[13] = inf['编码']
            value_list[14] = self.inf_sample_name
            value_list[19] = inf['测试结果']
            value_list[20] = inf['测试员']

            sht.range('a2').value = value_list
            wb.save()
            # wb.close()
            # app.quit()
            app.kill()
        else:
            wb = app.books.open(self.wb_path+file_name)      
            sht = wb.sheets[0]        

            for value in range(22):
                value = None
                value_list.append(value)  
            value_list[2] = inf['实际开始日期']
            value_list[3] = inf['报告日期']
            value_list[9] = inf['样品生产单位']
            value_list[10] = inf['样品编码']
            value_list[11] = inf['检测类别']
            value_list[12] = inf['委托人']
            value_list[13] = inf['编码']
            value_list[14] = self.inf_sample_name
            value_list[15] = inf['委托日期']
            value_list[16] = inf['计划开始日期']
            value_list[17] = inf['计划完成日期']
            value_list[19] = inf['测试结果']
            value_list[20] = inf['测试员']

            sht.range('a2').value = value_list
            wb.save(save_file_path)
            # wb.close()
            # app.quit()
            app.kill()

    def finish_excel(self,file_name = 'finish_plan.xlsx'):   
        inf = self.inf 
        app = xw.App(visible=False,add_book=False)
        save_file_path_plan = self.path+'/'+inf['编码']+'_计划表.xlsx'
        save_file_path_finish = self.path+'/'+inf['编码']+'_完成表.xlsx'

        if(os.path.exists(save_file_path_finish)):
            wb = app.books.open(save_file_path_plan)
            sht = wb.sheets[0]        
            get_value_list = sht.range('a2:v2').value
            app.kill()

            app2 = xw.App(visible=False,add_book=False)
            wb2 = app2.books.open(save_file_path_finish)
            sht2 = wb2.sheets[0]        
            value_list = sht2.range('a2:p2').value

            value_list = [get_value_list[13],get_value_list[9],get_value_list[14],get_value_list[10],get_value_list[12],get_value_list[15],get_value_list[15],get_value_list[11],get_value_list[18],get_value_list[20],get_value_list[17],get_value_list[3],get_value_list[13],get_value_list[19]]

            sht2.range('a2').value = value_list
            wb2.save()
            app2.kill()
        else:
            wb = app.books.open(self.wb_path+file_name)
            sht = wb.sheets[0]
            # value_list = create_value_list(16)
            value_list = [inf['编码'],inf['样品生产单位'],self.inf_sample_name,inf['样品编码'],inf['委托人'],inf['送样日期'],inf['送样日期'],inf['测试目的'],1,inf['测试员'],None,None,inf['编码'],"合格"]

            sht.range('a2').value = value_list

            wb.save(save_file_path_finish)
            # wb.close()
            # app.quit()
            app.kill()

    

