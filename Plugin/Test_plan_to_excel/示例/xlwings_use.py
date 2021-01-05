#引入库
import xlwings as xw

#打开Excel程序，默认设置：程序可见，只打开不新建工作薄
# app = xw.App(visible=True,add_book=False)
#程序不可见，只打开不新建工作簿
app = xw.App(visible=False,add_book=False)

#新建工作簿 (如果不接下一条代码的话，Excel只会一闪而过，卖个萌就走了）
# wb = app.books.add()

#打开已有工作簿（支持绝对路径和相对路径）
wb = app.books.open('D:\work_station\doc_auto\plugin\sample.xlsx')
#练习的时候建议直接用下面这条
#wb = xw.Book('example.xlsx')
#这样的话就不会频繁打开新的Excel

#引用工作表
sht = wb.sheets[0]
#sht = wb.sheets[第一个sheet名]

#引用单元格
#rng = sht.range('a1')
#rng = sht['a1']
#rng = sht[0,0] 第一行的第一列即a1,相当于pandas的切片

#引用区域
#rng = sht.range('a1:a5')
#rng = sht['a1:a5']
#rng = sht[:5,0]

#|||重头戏：写入数据|||
#(xlwings多个单元格的写入大多是以表格形式)
#选择起始单元格A1,写入字符串‘Hello’
# sht.range('a1').value = 'Hello'

# 默认按行插入：A1:D4分别写入1,2,3,4
# sht.range('a1').value = [1,2,3,4]
# 等同于
# sht.range('a1:d4').value = [1,2,3,4]

# 按列插入： A2:A5分别写入5,6,7,8
# sht.range('a2').options(transpose=True).value = [5,6,7,8]

# 多行输入就要用二维列表了：
# sht.range('a6').expand('table').value = [['a','b','c'],['d','e','f'],['g','h','i']]

# |||读取|||
# 读取A1:D4（直接填入单元格范围就行了）
# print(sht.range('a1:d4').value)

# 返回的值是列表形式，多行多列为二维列表，但有一点要注意，返回的数值默认是浮点数
# a = sht.range('a1:d4').value
# print(a)
# for i in a:
#   print(i)
#   print(type(i))

# 读取excel的第一列怎么做？
# a = sht.range('a:a').value
# print(len(a))

# 你将会得到一个1048576个元素的列表，也就是空值也包含进去了，所以这种方法不行
# 思路：先计算单元格的行数(前提是连续的单元格)
rng = sht.range('a1').expand('table')
# nrows = rng.rows.count
# print(nrows)
# 接着就可以按准确范围读取了
# a = sht.range(f'a1:a{nrows}').value
# print(len(a))

# 同理选取一行的数据也一样
ncols = rng.columns.count
#用切片
fst_col = sht[0,:ncols].value
print(len(fst_col))

#保存工作簿
wb.save('D:\work_station\doc_auto\plugin\sample.xlsx')

#退出工作簿（可省略）
wb.close()

#退出Excel
app.quit()