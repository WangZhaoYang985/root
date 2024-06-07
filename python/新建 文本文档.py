# -- coding: utf-8 --
import os
import shutil
from unittest import result

import xlrd
import pandas as pd

def findfiles(files_path, files_list, filename):
    # 查找文件代码
    files = os.listdir(files_path)  # 返回path目录下的文件和目录列表
    for s in files:
        s_path = os.path.join(files_path, s)  # 连接两个或多个path（os.path模块）
        if os.path.isdir(s_path):  # 判断path是否为目录
            findfiles(s_path, files_list, filename)  # 递归
        elif os.path.isfile(s_path) and filename in s:  # is.file(path)判断path是否为文件
            result.append(s_path)


# srcfile 需要复制、移动的文件
# dstpath 目的地址

def mycopyfile(srcfile, dstpath,kh,xm):  # 复制函数
    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
    else:
        fpath, fname = os.path.split(srcfile)  # 分离文件名和路径
        if "体检表" in fpath:
            fname = "体检表"+fname
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)  # 创建路径
        if not os.path.exists(dstpath + kh +" - "+ xm+" - 报名信息_files"+"/"):
            os.makedirs(dstpath + kh +" - "+ xm+" - 报名信息_files"+"/")
        if not os.path.exists(dstpath + kh +" - "+ xm+" - 成绩与志愿信息_files"+"/"):
            os.makedirs(dstpath + kh+" - "+xm+" - 成绩与志愿信息_files"+"/")
        if not os.path.exists(dstpath + kh+" - "+xm+" - 体检信息_files"+"/"):
            os.makedirs(dstpath + kh +" - "+ xm+" - 体检信息_files"+"/")
        shutil.copy(srcfile, dstpath + fname)  # 复制文件
        if fname == kh+".jpg" or fname == kh+".jpG" or fname == kh+".BMP":
            shutil.copy(srcfile, dstpath + "/"+kh +" - " +xm+" - 报名信息_files"+"/"+ fname)
            shutil.copy(srcfile, dstpath +"/"+ kh+ " - " +xm + " - 成绩与志愿信息_files" + "/" + fname)
            shutil.copy(srcfile, dstpath +"/"+ kh +" - "+ xm+" - 体检信息_files"+"/" + fname)
            print("copy %s -> %s" % (srcfile, dstpath + fname))
        print("copy %s -> %s" % (srcfile, dstpath + fname))


def mkdir_multi(path):
    # 判断路径是否存在
    isExists = os.path.exists(path)
    if not isExists:
        # 如果不存在，则创建目录（多层）
        os.makedirs(path)
        return True


df = pd.read_excel("F:/xjufe\招就办\新建 XLS 工作表.xls")
xingming = df['姓名'].tolist()
banji = df['班级'].tolist()
kaohao = df['考生号'].tolist()
xuehao = df['学号'].tolist()
yuanxi = df['录取院系'].tolist()
zhuanye = df['招生专业名称'].tolist()
path = r"F:\xjufe\招就办\2023招生录取材料电子存档\陕西-104"
for i in range(4520):
    考号 = str(int(round(kaohao[i], 0)))
    result = []
    findfiles(path, result, 考号)
    班级 = str(banji[i])
    专业 = str(zhuanye[i])
    姓名 = str(xingming[i])
    院系 = str(yuanxi[i])
    学号 = str(int(round(xuehao[i], 0)))
    mubiaopath = 'F:/xjufe/招就办文件/2023新生入学资格审查/' + 院系 + '/' + 专业 + '/' + 班级 + '/' + 班级 + ' '+学号 + 姓名 + '/'
    #mkdir_multi(mubiaopath)
    for srcfile in result:
        mycopyfile(srcfile, mubiaopath,考号,姓名)# 复制文件

