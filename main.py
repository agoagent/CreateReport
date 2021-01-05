# import common module
import sys,shutil,os,json

# from webapp.utils.logging import LOGGER

# # 未用到--- 模块化组件jinja2
# # import jinja2
# # from jinja2.utils import Markup

#set_path
from os import path
file_path = path.dirname(__file__)
file_father_path = os.path.dirname(file_path)

#import other module
sys.path.append(r'.\File_change')
from File_change import operate_file_inf

sys.path.append(r'.\Function')
from Function import Path
from Function import Operate_folder

sys.path.append(r'.\Function\Input')
from Function.Input import input_inf

sys.path.append(r'.\Function\Chinese_to_english')
from Function.Chinese_to_english import CtoE

sys.path.append('./Plugin')
from Plugin import xls
from Plugin import control_rar_files

sys.path.append(r'.\Function\Template')
from Function.Template import use_template

sys.path.append(r'.\Function\Common')
from Function.Common import common

sys.path.append(r'.\Plugin\Test_plan_to_excel')
from Plugin.Test_plan_to_excel.xlwings_change import Create_xlsl_by_test_inf

#----get file inf----
operate_file_inf.save_file_inf(file_path)
get_test_inf = operate_file_inf.load_file_inf(file_path)
#----end----

#----setting path----
file_out_put_name = Path.output_path(get_test_inf,'output_path',file_path)
file_folder_name = Path.output_path(get_test_inf,'folder_path',file_path)
file_path_name = Path.output_path(get_test_inf,'file_path',file_path)
file_path_add = Path.output_path(get_test_inf,'file_path_add',file_path)
file_path_add_other = Path.output_path(get_test_inf,'file_path_add_other',file_path)
file_path_add_app_report = Path.output_path(get_test_inf,'file_path_add_app_report',file_path)
#----end----

#----create folder----
target_path = file_out_put_name+file_folder_name
Operate_folder.mkdir(target_path)
Operate_folder.mkdir(target_path+'/information')
Operate_folder.mkdir(target_path+'/pic')
Operate_folder.mkdir(target_path+'/pic_oth')
# Operate_folder.mkdir(target_path+'/other')
#----end----

#----add input inf----
input_all = input_inf.input_inf(get_test_inf)
#----end----

#----add english inf----
context = dict(get_test_inf, **input_all)
enligsh_inf = CtoE.CtoE(context)
#----end----

#----get download file:xls----
test_plan_inf = xls.read_xls_file(context['编码'],file_path)
input_cum = context['不合格数']+context['不使用数']+context['未检测数']
xls_plan = xls.output_xls(test_plan_inf,input_cum)
context = dict(context, **xls_plan)
test_item_path = '.'+file_folder_name+'/information/'+'test_item.txt'
common.save_file(file_folder_name,test_plan_inf,'test_item.txt',file_path)
#----end----

#----get download file:rar----
control_rar_files.operate_rar_files(context['编码'],file_path)
#----end----

#---- add inf to dict----
context = dict(context, **enligsh_inf)
#----end----

#----update and save dict file----
context = operate_file_inf.update_file_inf(context,file_folder_name,'test_value.txt')
common.save_file(file_folder_name,context,'test_value.txt',file_path)
#----end----

#----read template----
tpls = use_template.read_template(context)
tpl_main = tpls[0]
tpl_ohter =tpls[1]
tpl3_app_other =tpls[2] 
tpl4_app_report = tpls[3]
#----end----

#----loading pic----
tpl_pic = use_template.setpictosrc(file_path,context['检测类别'],tpl_main,common.findpic(file_folder_name,'pic',file_path),file_folder_name)
tpl_pic_2 = use_template.setpictosrc(file_path,context['检测类别'],tpl_ohter,common.findpic(file_folder_name,'pic_oth',file_path),file_folder_name, 'other')
#----end----

#----add pic to dict----
context = dict(context, **tpl_pic, **tpl_pic_2)
#----end----

#----test_plan_excel----
#xlwings处理计划表与完成表
plan_excel = file_out_put_name+file_folder_name+'/xlwings_output'
Operate_folder.mkdir(plan_excel)
Create_xlsl_by_test_inf(plan_excel,context).plan_excel()
Create_xlsl_by_test_inf(plan_excel,context).finish_excel()
#----end----

#----out put template----
tpl_main.render(context)
tpl_main.save(file_out_put_name+file_folder_name+file_path_name)

tpl_ohter.render(context)
tpl_ohter.save(file_out_put_name+file_folder_name+file_path_add)

if("埋点" in context['整体说明']):
    tpl3_app_other.render(context)
    tpl3_app_other.save(file_out_put_name+file_folder_name+file_path_add_other)

if("APP测试" in context['检测类别']):
    if(file_path_add_app_report != ''):
        tpl4_app_report.render(context)
        tpl4_app_report.save(file_out_put_name+file_folder_name+file_path_add_app_report)
#----end----

#----finish delete download file----
xls.remove_xls()
control_rar_files.remove_rar_files(context['编码'],file_path)
#----end----