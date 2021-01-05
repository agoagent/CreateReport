import json,os,re,sys
from os import path

import setting

sys.path.append(r'.\Function\Common')
from Function.Common import common

file_path = path.dirname(__file__)
file_father_path = os.path.dirname(file_path)

#输入信息路径
files_inf_c = file_path+"/auto_file_in.txt"
#输出信息路径
files_inf_output = file_path+"/auto_file_output.txt"

def save_file_inf(path):
	files = open(files_inf_c,"r",encoding="utf-8")
	get_datas = files.readlines()
	# print(len(get_data))
	# exit()

	#筛选纯换行
	get_data = []
	for get_data_value in get_datas:
		if(get_data_value != '\n'):
			get_data.append(get_data_value)

	if(len(get_data) > 0):
		get_data_chose = get_data
		# print(get_data)
		files.close
		# exit()

		#变成字典
		get_data_chose_select_cum = {}
		#for循环1,2 2,3 3,4对比
		for get_data_num,get_data_dirc in enumerate(get_data):
			get_data_index = get_data[get_data_num]
			try:
				get_data_value = get_data[get_data_num+1]
			except IndexError:
				break

      #筛选异常，过滤关键字
			if(get_data_index.find(":\n") != -1 and get_data_value.find(":\n") == -1):
				if(get_data_index.find("委托部门") != -1 and get_data_value.find(":\n") == -1):
					get_data_value = get_data_value[get_data_value.rfind('_')+1:]

				if(get_data_index.find("委托人") != -1 and get_data_value.find(":\n") == -1):
					get_data_value = get_data_value[0:get_data_value.rfind('('):]

				if(get_data_value.find("<") != -1 and get_data_value.find(">") != -1):
					get_data_value = get_data_value.replace('<','[').replace('>',']')

				if (get_data_index.find(" ") > 0):
					get_data_index = get_data_index.replace(' ','')
					
				# print(get_data_index)
				get_data_index = get_data_index.replace(':\n','')
				get_data_value = get_data_value.replace('\n','')
				get_data_chose_select_cum[get_data_index] = get_data_value
		# print(json.dumps(get_data_chose_select_cum,ensure_ascii=False,sort_keys=True,indent=1))
		# print(get_data_chose_select_cum)
		
		#add subject test value
		if('插件' in get_data_chose_select_cum['样品名称']):
			get_data_chose_select_cum['检测类别'] = 'APP测试'
		else:
			if('首样' in get_data_chose_select_cum['整体说明']):
				get_data_chose_select_cum['检测类别'] = '首样测试'
			else:
				get_data_chose_select_cum['检测类别'] = '变更测试'
		# print(get_data_chose_select_cum)

		#app_name
		target_app_list = setting.global_inf('global_target_app_list')
		app_name =''
		for target_app_name in target_app_list:
				if(target_app_name in get_data_chose_select_cum['样品名称']):
						app_name = target_app_name+'插件'
		get_data_chose_select_cum['app类型'] = app_name

		#批量运行时使用
		# files_inf = r"D:\work_station\doc_auto\file_change\auto_file_output_"+get_data_chose_select_cum['编码']+r'.txt'

		files_inf = file_path+"/auto_file_output.txt"
		get_data_chose_select_cum = json.dumps(get_data_chose_select_cum,ensure_ascii=False,sort_keys=True,indent=1)
		files = open(files_inf,"w",encoding="utf-8")
		files.write(get_data_chose_select_cum)
	else:
		files = open(files_inf_output,"r",encoding="utf-8")
		get_data = files.readlines()
		if(len(get_data) == 0):
			print('未检测到委托信息，请输入后再执行')
			exit()
	files.close

def load_file_inf(path):
	#读取文件里面的数据
	context = {}
	files_inf = "./File_change/auto_file_output.txt"
	files = open(path+files_inf,"r",encoding="utf-8")
	context = json.load(files)
	files.close
	return(context)

def update_file_inf(inf,target_file_path,target_file_name):
	target_file = './Report'+target_file_path+'/information/'+target_file_name
	if(os.path.exists(target_file)):
		context = common.read_file(target_file)
		inf['送样日期'] = context['送样日期']
	return inf
	



# save_file_inf()
# print(load_file_inf())