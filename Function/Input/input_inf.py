import time,sys,json,os
sys.path.append(r'.\Function\Input')
from Function.Input import input_inf_func
from os import path

app_tester = 'name3'
app_test_result = '通过'

def input_inf(inf):
  context = inf
  list_misson_project_nums = ''
  context2 = {
      "环境温度":"26",
      "相对湿度":"60",
      "测试部门": "test_name_1",
      "送样日期": input_inf_func.get_set_time(context,"送样日期",""),
      "完成日期": input_inf_func.report_time_set(""),
      "报告日期": input_inf_func.report_time_set(""),
      "测试员": app_tester,
      "审核员":"name1",
      "审批员":"name2",
      "测试结果":"合格",
      "测试目的":context['检测类别'],
      "测试代号":list_misson_project_nums,
      "计划开始日期":input_inf_func.date_change(input_inf_func.get_set_time("送样日期",""),"1day"),
      "计划完成日期":input_inf_func.date_change(input_inf_func.get_set_time("送样日期",""),"1week"),
      "实际开始日期":"",
      "实际完成日期":"",
  }

  get_datas = {}
  file_path = path.dirname(__file__)
  files_path = file_path+"/../Dirt/phone_information.txt"
  files = open(files_path,"r",encoding="utf-8")
  get_datas = json.load(files)
  files.close

  all_app_context = ''
  for get_data_key,get_data_value in get_datas.items():
    keylist = get_data_key.split('_')
    valuelist = get_data_value.split(',')
    name = keylist[0]+'_name_'+keylist[2] 
    sys = keylist[0]+'_sys_'+keylist[2]
    app_tester_name = 'app_tester_'+keylist[2]
    app_test_result_name = 'app_test_result_'+keylist[2]
    resolution = keylist[0]+"_resolution_"+keylist[2]
    if("测试版" in context['整体说明']):
      app_context = {name:valuelist[0],sys:valuelist[1],resolution:valuelist[2],app_tester_name:app_tester,app_test_result_name:app_test_result}
    else:
      if("1" == keylist[2]):
        app_context = {name:valuelist[0],sys:valuelist[1],resolution:valuelist[2],app_tester_name:app_tester,app_test_result_name:app_test_result}
    all_app_context = dict(all_app_context,**app_context)

  app_context_white_box = {
      "APP版本":"6.5",
      "埋点APP版本":"6.5",
  }

  others = {
      "Description_of_sample":"",
  }

  default = {
    "委托数":"/",
    "合格数":"/",
    "不合格数":0,
    "不使用数":0,
    "未检测数":0,
  }

# #附加表内容
# add_context = {
#     "EMC测试员":"name4",
#     "环境测试员":"name5",
# }


  inf_all = dict(context2, **all_app_context, **app_context_white_box, **others, **default)
  return(inf_all)

def input_inf_other(inf):
  pass