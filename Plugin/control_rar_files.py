import sys,os,shutil

sys.path.append("././Function/Common")
from Function.Common import common

sys.path.append('./Plugin/Test_plan_to_excel')
from Plugin.Test_plan_to_excel import output_excel
from Plugin.Test_plan_to_excel.output_excel import Print_out_misson_value
from Plugin.Test_plan_to_excel.output_excel import Print_out_misson_project
from Plugin.Test_plan_to_excel.output_excel import Find_file

# 读取rar的委托文件包
def operate_rar_files(inf,file_path):
    context = {'编码':inf}
    test_item_file_paths_rar = output_excel.Find_file('none').findfile('zip','D:\MyData\pengjw3\Downloads','-附件')
    target_folder_path = common.find_folder(file_path+'/Report',context['编码'])

    if(os.path.exists(target_folder_path+'\委托资料') == False):
        if test_item_file_paths_rar != []:
            if context['编码'] in test_item_file_paths_rar[0]:
                pass
            else:
                print("压缩文件错误，请重新下载:"+context['编码']+'!='+test_item_file_paths_rar[0])
                exit()
            shutil.copy(test_item_file_paths_rar[0],target_folder_path)
            target_test_item_file_paths_rar = output_excel.Find_file('none').findfile('zip',target_folder_path,'-附件')
        #解压rar
            import zipfile
            # os.chdir(r"D:\软件\pychar\data\test")
            z = zipfile.ZipFile(target_test_item_file_paths_rar[0],'r')
            # print(test_item_file_paths_rar[0])
            z.extractall(target_folder_path+'\委托资料')
            z.close()
        else:
            if(context['编码']):
                if(os.path.exists(target_folder_path+'\委托资料')):
                    pass
                else:
                    print(context['编码']+"未能查询到压缩文件"+",未下载压缩文件，请下载再试")
                    exit()
            else:
                print("错误,未查询到压缩文件")
    # print(test_item_file_paths_rar[0])

def remove_rar_files(inf,file_path):
  #删除委托资料压缩包
    context = {'编码':inf}
    test_item_file_paths_rar = output_excel.Find_file('none').findfile('zip','D:\MyData\pengjw3\Downloads','-附件')
    if(test_item_file_paths_rar):
        # target_folder_path = common.find_folder(file_path+'/Report',context['编码'])
        os.remove(test_item_file_paths_rar[0])
        # print('remove')