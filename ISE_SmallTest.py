# -*- coding: utf-8 -*-

import Tkinter
import tkMessageBox
import tkFileDialog
import csv

root=Tkinter.Tk()
root.withdraw()

fTyp=[('CSVファイル','.csv')]
#複数のタイプを指定することも可能。

#Windows用
iDir='c:/'

#askopenfilename 一つのファイルを選択する。 filrname:選択したファイルのパス
filename1=tkFileDialog.askopenfilename(filetypes=fTyp,initialdir=iDir)
tkMessageBox.showinfo('FILE NAME is ...',filename)

#上で選択したCSVファイルを読み込み
f = open(filename, 'rb')
dataReader = csv.reader(f)

#読み込んだデータそのまま
data = [ v for v in dataReader]
#回答部分だけの配列
=[[0 for i in range(len(data[0])-1)] for j in range(len(data))]
#学籍番号部分だけの配列
stnum=len(data)*[0]

#学生番号と回答を分割するfor文
for row in range(0,len(data)):
	stnum [row] = data[row][0]
	for column in range(1,len(data[0])):
		ans[row][column-1] = data[row][column]

#回答部分をint型に
ans_conved = [[int(elm) for elm in v] for v in ans]

#一旦表示
print(stnum)
print(ans)
