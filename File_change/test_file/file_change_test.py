import re

files_inf = r"D:\work_station\doc_auto\file_change\auto_file_c.txt"
files = open(files_inf,"r",encoding="utf-8")
get_data = files.readlines()
# print(get_data)
important_word = ":\n"
get_data_address = [i for i, x in enumerate(get_data) if x.find(important_word) !=-1]
print(get_data_address)
# index = list
# for num,index_line in enumerate(get_data):
#     if (index_line.find(":\n")) != -1:
        # index_line = index_line.strip() 
        # index.append(index_line)
        # if num in get_data_address:
                # print(index_line)

# print(get_data[2])
files.close

#获取list符合的元素位置
# get_data_address = [i for i, x in enumerate(get_data) if x.find(important_word) !=-1]

#参考 查询list位置方法 #不适用list
# import re
# word = "test"
# s = "test abcdas test 1234 testcase testsuite"
# w = [m.start() for m in re.finditer(word, s)]
# print(w)

#参考 过滤方法
# list_string= ['big', 'letters']
# list_text = ['hello letters', 'big hi letters', 'big superman letters']
# all_words = list(filter(lambda text: all([word in text for word in list_string]), list_text ))
# print(all_words) 
#['big hi letters', 'big superman letters']

# filter方法分离 弃用
# list_chose = [':\n']
# index = list(filter(lambda text: all([word in text for word in list_chose]), get_data ))
# print(index)
# for index_line in index:
#         index_line = index.strip() 
#         print(index_line)

#过滤出目录 弃用
# list = []
# index = list
# for index_line in get_data:
#     if (index_line.find(":\n")) != -1:
#         index_line = index_line.strip() 
#         index.append(index_line)
        # print(index)
# print(index)

#过滤出属性 弃用
# value = list
# for value_line in get_data:
#     if (value_line.find(":\n")) == -1:
#         value_line = value_line.strip() 
#         value.append(value_line)
#         # print(value)
# # print(value)

#目录属性未分离，待解决
#思路 输入到字典再输出
# print(index+value)

