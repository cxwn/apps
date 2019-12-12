# -*- coding:utf-8 -*-
import os, xlrd, xlsxwriter, time, sys

source_dir = r'input'
new_execl = str(time.time()).split('.')[0] + '.xlsx'
raw_excels = []
keyword = "油站经理" # 带此关键字的行不是有效行，不插入
data = []

confirm = input("请将需要处理的 Excel 文件保存到当前文件夹的 input 文件夹下面，确认请按：Y/y，按其他键退出本程序！输入之后请按回车，请确认:")
if confirm == 'Y' or confirm == 'y':
    pass
else:
    print("程序正在退出... ...")
    time.sleep(5)
    exit()

if os.path.exists(os.path.join(os.getcwd(), source_dir)) and len(os.listdir(source_dir)):
    raw_excels = os.listdir(source_dir)
else:
    print("input 文件夹有误，请确认！")
    time.sleep(10)
    exit()

filename = os.path.join(source_dir, raw_excels[0])
wb = xlrd.open_workbook(filename)
sheet = wb.sheets()[0]
data.append(sheet.row_values(0))
data.append(sheet.row_values(1))

for excel in raw_excels:
    filename = os.path.join(source_dir, excel)
    wb = xlrd.open_workbook(filename)
    sheet = wb.sheets()[0]
    for row_num in range(2, sheet.nrows):
        row_values = [str(i) for i in sheet.row_values(row_num)]
        row_values[0] = ''
        row_values[1] = ''
        if len(''.join(row_values)) and (keyword not in ''.join(row_values)):
            print('插入的行在文件\"{0}\"中, 插入的内容为：'.format(excel), end = '')
            print(sheet.row_values(row_num))
            data.append(sheet.row_values(row_num))

# 更新序号
print('\n\n')
for serial in range(2,len(data)):
    if serial > 1:
        data[serial][0] = serial - 1

# 写入新的 Excel 文件
files = str(len(raw_excels))
lines = str(len(data) - 2)
print("处理进度如下：\n\n")
new_wb = xlsxwriter.Workbook(new_execl)
worksheet = new_wb.add_worksheet()
font = new_wb.add_format({"font_size":11})
for i in range(len(data)):
    for j in range(len(data[i])):
        worksheet.write(i, j, data[i][j], font)
        print('█', sep = ' ', end = '')
print('\n')
new_wb.close()

print("本次处理的文件数量：{fs}，新表格除去标题及表头的总行数为：{ls}。处理完毕，合并后的新文件在当前文件夹下，新文件名称为：{nf}".format(fs = files, ls = lines, nf = new_execl) + "，欢迎再次使用！\n")
print("作者：IVAN DU，2019-12-09于北京！\n")
print("版权所有，侵权必究!\n")
os.system("pause")