def output_path(inf,type,file_path):
	context = inf
	if(context['产品大类'] == '洗碗机'):
		add_table_name = '原始记录'
	else:
		add_table_name = '_附表'

	if('校验码' in context.keys()):
			check_code = '_'+context['校验码']
	else:
			check_code = ''
	#app_name
	target_app_list = ['美居','小京鱼','苏宁','布谷','天猫']
	for target_app_name in target_app_list:
			if(target_app_name in context['样品名称']):
					app_name = target_app_name+'插件'
					break
			else:
					app_name = ''

	if(type == 'output_path'):
		file_out_put_name = file_path+'/report'
		return(file_out_put_name)
	elif(type == 'folder_path'):
		file_folder_name ='/'+context['编码']+'_'+context['样品编码']+'_'+context['样品型号']+'_'+context['样品生产单位']+'_'+context['检测类别']+'_'+app_name+'评价报告'
		return(file_folder_name)
	elif(type == 'file_path'):
		file_path_name = '/'+context['编码']+'_'+context['样品编码']+'_'+context['样品型号']+check_code+'_'+context['样品生产单位']+'_'+context['检测类别']+'_'+app_name+'评价报告'+r'.docx'
		return(file_path_name)
	elif(type == 'file_path_add'):
		file_path_name_add = '/'+context['编码']+'_'+context['样品编码']+'_'+context['样品型号']+check_code+'_'+context['样品生产单位']+'_'+context['检测类别']+'_评价报告'+add_table_name+r'.docx'
		return(file_path_name_add)
	elif(type == 'file_path_add_other'):
		file_path_name_app_add = '/'+context['编码']+'_'+context['样品编码']+'_'+context['样品型号']+check_code+'_'+context['样品生产单位']+'_'+context['检测类别']+'_'+app_name+'埋点数据测试报告'+r'.docx'
		return(file_path_name_app_add)
	elif(type == 'file_path_add_app_report'):
		if(app_name == '美居插件'):
			file_path_add_app_report = '/'+'美的美居APP_'+context['样品型号']+'插件_测试报告'+r'.docx'
		else:
			file_path_add_app_report = ''
		return(file_path_add_app_report)