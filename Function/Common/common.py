import os,json,shutil

#用value找key函数
def get_key (dict, value):
    return [k for k, v in dict.items() if v == value]

#读取文件
def read_file(target_path):
    files = open(target_path,"r",encoding="utf-8")
    set_dict = json.load(files)
    # print(set_dict)
    # exit()
    files.close
    return(set_dict)

#保存文件
def save_file(target_path,inf,targe_file,file_path):
    #保存xls处理文件
    test_item = open(file_path+'/Report'+target_path+'/information/'+targe_file, 'w+',encoding='UTF-8')
    save_test_item = json.dumps(inf,ensure_ascii=False,sort_keys=True,indent=1)
    test_item.write(save_test_item)
    test_item.close()

#查找图片
#文件路径，图片路径，执行文件根路径
def findpic(file_path,pic_path,path):
    file_path = path+'/Report'+file_path+'/'+pic_path
    filelists = []
    filelist = os.listdir(file_path)
    for filename in filelist:
        if ".jpg" in filename or ".png" in filename:
            filelists.append(filename)
    # print(filelists)
    return filelists

#输出文件信息到目的地并更改名称
def file_rename(file_path,new_file_path,new_file):
  if(os.path.exists(file_path)):
      pass
  else:
      shutil.copy(file_path,new_file_path)
      os.rename(new_file_path,new_file)
  #end


#查询文件夹
def find_folder(file_path, target_folder_name):
    father_folder_list = os.listdir(file_path)
    for folder in father_folder_list:
        if target_folder_name in folder:
            return file_path+'/'+folder