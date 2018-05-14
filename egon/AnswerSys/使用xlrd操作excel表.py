#使用方法
'''
导入
import xlrd
打开excel
data = xlrd.open_workbook('demo.xls') #注意这里的workbook首字母是小写
查看文件中包含sheet的名称
data.sheet_names()
得到第一个工作表，或者通过索引顺序 或 工作表名称
table = data.sheets()[0]
table = data.sheet_by_index(0)
table = data.sheet_by_name(u'Sheet1')
获取行数和列数
nrows = table.nrows
ncols = table.ncols
获取整行和整列的值（数组）
table.row_values(i)
table.col_values(i)
循环行,得到索引的列表
for rownum in range(table.nrows):
print table.row_values(rownum)
单元格
cell_A1 = table.cell(0,0).value
cell_C4 = table.cell(2,3).value
分别使用行列索引
cell_A1 = table.row(0)[0].value
cell_A2 = table.col(1)[0].value
'''

#使用
import xlrd
data=xlrd.open_workbook(r'/Users/jieli/PycharmProjects/爬虫/t1/AnswerSys/test.xlsx')

table=data.sheets()[0]
print(table.nrows)
print(table.ncols)


print(table.row_values(3))
print(table.col_values(0))

for i in range(table.nrows):
    print(table.row_values(i))

print(table.cell(1,1).value)

#操作test.xlsx
subject={
    'type':None,
    'choice':[],
    'res':set(),
}
for i in range(2,table.nrows):
    row=table.row_values(i)
    if len(subject['choice'])==4:
        print(subject)
        subject={
            'type':None,
            'choice':[],
            'res':set()
        }
    if row[0]:
        subject['type']=row[0]
    else:
        subject.setdefault('choice').append(row[2])
        if row[3] == 1:
            res_str=row[2].strip()
            res=res_str[0].upper()
            subject['res'].add(res)

else:
    print(subject)