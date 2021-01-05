import os
from os import path
template_file_path = path.dirname(__file__)
template_file_father_path = os.path.dirname(template_file_path)

import docxtpl
from docxtpl import DocxTemplate, InlineImage
# for height and width you have to use millimeters (Mm), inches or points(Pt) class :
from docx.shared import Mm, Inches, Pt

def read_template(inf):
  context = inf
  # module_name:使用模板名称
  file_path = template_file_path+'/Use'
  if (context['产品大类'] == '洗碗机'):
      module_name = '洗碗机报告模板2019C'
  else:
      module_name = '报告模板2019C'
  tpl = DocxTemplate(file_path+'/'+context['app类型']+module_name+'.docx')
#   print(context)
  tpl2 = DocxTemplate(file_path+'/'+context['app类型']+module_name+'_附表.docx')
  tpl3 = DocxTemplate(file_path+'/埋点数据测试报告模板.docx')
  tpl4 = DocxTemplate(file_path+'/App插件测试报告模板.docx')
  tpls = [tpl,tpl2,tpl3,tpl4]
  return tpls

  # #循环输出图片到目标 -- 使用，使用循环识别进行处理
def setpictosrc(path,check_app,tpl,filelists,file_path,use_tab = ''):
    context_pic = {}
    if filelists:
        for file_count,file_name in enumerate(filelists):
            file_path_output = path+'/Report'+file_path+'/pic/'+filelists[file_count]
            # context_pic_key = 'productPic'+str(file_count)
            if(use_tab == ''):
                if(file_count == 0):
                    context_pic_key = 'fornt_side'
                elif(file_count == 1):
                    context_pic_key = 'back_side'
                elif(file_count == 2):
                    context_pic_key = 'label'
                else:
                    context_pic_key = 'null'+str(file_count)
            else:
                context_pic_key = use_tab+str(file_count)

            if(check_app == ''):
                context_pic_value = InlineImage(tpl,file_path_output, width=Mm(60))
            else:
                context_pic_value = InlineImage(tpl,file_path_output, width=Mm(40))
                if(file_count == 2):
                    context_pic_value = InlineImage(tpl,file_path_output, width=Mm(80))
            context_pic.update({context_pic_key:context_pic_value})
    return(context_pic)

# 检测目标图片名称并输出  --停用，使用固定名字进行识别
def get_name_to_setpictosrc(check_app,tpl,filelists,file_path,use_tab = ''):
    context_pic = {}
    target_name = ''
    if filelists:
        for file_count,file_name in enumerate(filelists):
            file_path_output = '././Report'+file_path+'/pic/'+filelists[file_count]
            if(check_app == ''):
                context_pic_value = InlineImage(tpl,file_path_output, width=Mm(60))
            else:
                context_pic_value = InlineImage(tpl,file_path_output, width=Mm(40))
                if(file_count == 2):
                    context_pic_value = InlineImage(tpl,file_path_output, width=Mm(80))

            for key_name,value_name in file_name.items():
                if(key_name in file_path_output):
                    target_name = value_name
            context_pic.update({target_name:context_pic_value})
    return(context_pic)