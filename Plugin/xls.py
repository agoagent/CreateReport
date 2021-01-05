import json,sys,os
from os import path
file_path = path.dirname(__file__)
file_father_path = os.path.dirname(file_path)

sys.path.append("././Function/Common")
from Function.Common import common

sys.path.append('./Plugin/Test_plan_to_excel')
from Plugin.Test_plan_to_excel import output_excel
from Plugin.Test_plan_to_excel.output_excel import Print_out_misson_value
from Plugin.Test_plan_to_excel.output_excel import Print_out_misson_project
from Plugin.Test_plan_to_excel.output_excel import Find_file

switch = True

if(switch):
  #读取xls的委托项
  test_item_file_paths = output_excel.Find_file('none').findfile('xls','D:\MyData\pengjw3\Downloads','pengjw3')
  misson_project_nums = []
  save_test_item = {}
  save_test_file_value = {}
  download_file = ''
  TestProject = {}

def read_xls_file(inf,file_path):
  if(switch):
    context_num = inf
    target_folder_path = common.find_folder(file_path+'/Report',context_num)
    target_folder_path = target_folder_path+'\\information\\test_item.txt'
    
    if(test_item_file_paths == []):
      download_file = ''
      if(os.path.exists(target_folder_path)):
        if(download_file == ''):
          files = open(target_folder_path,"r",encoding="utf-8")
          misson_projects = []
          values = files.read()
          save_test_file_value = json.loads(json.dumps(eval(values)))
          return save_test_file_value
      else:
        print(target_folder_path+"未能查询到委托文件"+",未下载委托测试项文件，请下载再试")
        exit()
    else:
      misson_projects = Print_out_misson_project('none').read_excel(test_item_file_paths[0])
      download_file = test_item_file_paths[0]

    #处理xls的委托项，转化为数字
    TestProject = common.read_file(file_father_path+'/Function/Dirt/TestProject.txt')
    for misson_project in misson_projects:
        for text,num in TestProject.items():
            if text in misson_project:
                misson_project_nums.append(num)
                k = text
                v = num
                save_test_item.update({k:v})
    # 转换为int排序再转换回str
    list_misson_project_nums = misson_project_nums
    list_misson_project_nums_list = list(map(int, list_misson_project_nums))
    list_misson_project_nums_list.sort()
    list_misson_project_nums = list(map(str, list_misson_project_nums_list))
    return(list_misson_project_nums)

def output_xls(test_plan_inf_list,input_cum):
  test_plan_inf_list_num = len(test_plan_inf_list)
  output_inf ={
    "委托数":test_plan_inf_list_num,
    "合格数":test_plan_inf_list_num - input_cum,
  }
  return output_inf
  
def read_xls():
  if(test_item_file_paths != []):
    misson_projects = Print_out_misson_project('none').read_excel(test_item_file_paths[0])
    download_file = test_item_file_paths[0]
    return download_file

def remove_xls():
  if(test_item_file_paths != []):
    misson_projects = Print_out_misson_project('none').read_excel(test_item_file_paths[0])
    download_file = test_item_file_paths[0]
    if(download_file != None):
      os.remove(download_file)