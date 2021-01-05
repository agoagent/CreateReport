import os,json,sys
from os import path
file_path = path.dirname(__file__)
file_father_path = os.path.dirname(file_path)

#中英转换 进入中英转换的文件路径
sys.path.append(r'.\Function\Common')
from Function.Common import common
chinese_to_english_dict = {}
chinese_to_english_dict = common.read_file(file_path+r"\CtoE.txt")
# print(chinese_to_english_dict)
# exit()

def CtoE(inf):
  chinese_to_english = {}
  context = inf
  #列出字典的key和value,再使用第二本字典进行英文转换
  for k, v in context.items(): #items() 返回可遍历的(键, 值) 元组数组
      for english,chinese in chinese_to_english_dict.items():
          if (v == english):
              if(k in chinese_to_english_dict):
                  k = chinese_to_english_dict[k]
                  v =  chinese_to_english_dict[english]
                  chinese_to_english.update({k:v})
          # print(chinese_to_english)
  return(chinese_to_english)