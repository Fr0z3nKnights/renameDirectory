"""
@author:Fr0z3n
@contact:websec@yeah.net
@datetime:2020/4/28
@desc:
"""

import os,sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt


class batAction(QTabWidget):
    def __init__(self):
        super(batAction, self).__init__()
        self.tab1 = batCreatDir()
        self.tab2 = batModifydir()
        self.setWindowTitle("批量文件夹工具 v1.0 ------河南省煤田地质局四队物探测绘研究院 版权所有®")
        self.addTab(self.tab1,"Tab 1")
        self.addTab(self.tab2,"Tab 2")
        self.setTabText(0,'批量创建新文件夹')
        self.setTabText(1,'批量修改文件夹名')
        self.setWindowIcon(QIcon('./airplane.ico'))

class batModifydir(QWidget):
    def __init__(self):
        super(batModifydir, self).__init__()
        hlayout = QHBoxLayout()
        vlayout = QVBoxLayout()
        h2layout = QHBoxLayout()
        h3layout = QHBoxLayout()
        self.dirpath2 = QLineEdit()
        self.dirpath2.setPlaceholderText('请点击右侧按钮找到存放"所有需改名文件夹"的文件夹')
        self.lfilepath = QLabel()
        self.lfilepath.setText('文件路径：')
        self.lfilepath.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.dirpath2.setMinimumSize(400,20)
        self.dirpath2.setMaximumSize(400,20)
        self.btnopenfile = QPushButton(str('打开文件'))
        self.btnopenfile.clicked.connect(self.openfile)
        self.rbadd = QRadioButton('增加文件夹名前面字符')
        self.rbdel = QRadioButton('删除文件夹名前面某些字符')
        self.lchars = QLineEdit()
        self.lchars.setPlaceholderText('请输入要添加或者修改的字符')
        self.btnmdf = QPushButton('开始修改')
        self.btnmdf.clicked.connect(self.batmdfdir)
        self.dirlist2 = QListWidget()
        self.dirlist2.setViewMode(0)
        self.stbar2 = QStatusBar()
        self.rbadd.setChecked(True)
        # self.stbar.setStyle(QFrame.Panel | QFrame.Sunken)

        hlayout.addWidget(self.lfilepath)
        hlayout.addWidget(self.dirpath2)
        hlayout.addWidget(self.btnopenfile)
        h2layout.addWidget(self.rbadd)
        h2layout.addWidget(self.rbdel)
        h3layout.addWidget(self.lchars)
        h3layout.addWidget(self.btnmdf)

        hw = QWidget()
        hw.setLayout(hlayout)
        hw2 = QWidget()
        hw2.setLayout(h2layout)
        hw3 = QWidget()
        hw3.setLayout(h3layout)

        vlayout.addWidget(hw)
        vlayout.addWidget(self.dirlist2)
        vlayout.addWidget(hw2)
        vlayout.addWidget(hw3)
        vlayout.addWidget(self.stbar2)
        self.setLayout(vlayout)

        self.stbar2.showMessage("准备就绪.")
        self.filepath = ''


    def batmdfdir(self):
        try:
            i = 0
            j = 0
            addordel = self.lchars.text()
            print(self.filepath)
            os.chdir(self.filepath)
            addlist = []
            dellist = []
            if self.filepath:
                if self.rbadd.isChecked():
                    if addordel:
                        for li in os.listdir(self.filepath):
                            if os.path.isdir(self.filepath +'/' + li):
                                print("当前文件夹：%s" % li)
                                new = str(addordel) + str(li)
                                print("修改后名字：",new)
                                os.rename(li,new)
                                addlist.append(new)
                                i += 1
                        strms = "增加字符操作,文件夹名批量修改成功%s个" % i
                        self.dirlist2.clear()
                        self.dirlist2.addItems(addlist)
                        self.stbar2.showMessage(strms)
                        QMessageBox.about(self, "提示",strms)
                    else:
                        QMessageBox.about(self,"提示","操作字符为空，请填写字符再操作！")
                elif self.rbdel.isChecked():
                    if addordel:
                        for li in os.listdir(self.filepath):
                            if os.path.isdir(self.filepath +'/' + li):
                                new = li.replace(addordel,"")
                                j += 1
                                if new:
                                    print("当前文件夹：%s" % li)
                                    os.rename(li,new)
                                    print("修改后名字：", new)
                                    dellist.append(new)
                                    i += 1
                        self.dirlist2.clear()
                        self.dirlist2.addItems(dellist)
                        strms = "删除字符操作,文件夹名批量修改成功%s个" % i
                        self.stbar2.showMessage(strms)
                        QMessageBox.about(self, "提示", strms)
                    else:
                        QMessageBox.about(self, "提示", "操作字符为空，请填写字符再操作！")
            else:
                QMessageBox.about(self, "提示", "路径为空,请检查！")
        except Exception as e:
            ms = "修改文件夹名出错,%s" % e.args
            self.stbar2.showMessage(ms)
            QMessageBox.about(self,"警告",ms)


    def openfile(self):
        try:
            dlist = []
            self.dirlist2.clear()
            self.filepath = QFileDialog.getExistingDirectory(self,
                                                        "选择文件夹",
                                                        "d:/")
            # print(self.filepath)
            self.dirpath2.setText(self.filepath)
            for li in os.listdir(self.filepath):
                # print(li)
                if os.path.isdir(self.filepath + '/' + li):
                    dlist.append(li)
            print("文件夹列表：",dlist)
            self.dirlist2.addItems(dlist)
        except Exception as e:
            ms = "批量修改文件夹名出错,%s" % e.args
            self.stbar2.showMessage(ms)
            QMessageBox.about(self, "提示", ms)

class batCreatDir(QWidget):
    def __init__(self):
        super(batCreatDir,self).__init__()
        hlayout = QHBoxLayout()
        vlayout = QVBoxLayout()
        self.dirpath = QLineEdit()
        self.dirpath.setPlaceholderText('请点击右侧按钮找到存放"预创建文件夹名列表".txt')
        self.lfilepath = QLabel()
        self.lfilepath.setText('文件路径：')
        self.lfilepath.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.dirpath.setMinimumSize(400,20)
        self.dirpath.setMaximumSize(400,20)
        self.btnopenfile = QPushButton(str('打开文件'))
        self.btnopenfile.clicked.connect(self.batcrtdir)
        self.dirlist = QListWidget()
        self.dirlist.setViewMode(0)
        self.stbar = QStatusBar()
        # self.stbar.setStyle(QFrame.Panel | QFrame.Sunken)

        hlayout.addWidget(self.lfilepath)
        hlayout.addWidget(self.dirpath)
        hlayout.addWidget(self.btnopenfile)
        hw = QWidget()
        hw.setLayout(hlayout)

        vlayout.addWidget(hw)
        vlayout.addWidget(self.dirlist)
        vlayout.addWidget(self.stbar)
        self.setLayout(vlayout)

        self.stbar.showMessage("准备就绪.")
        self.items = []

    def batcrtdir(self):
        try:
            self.items.clear()
            newitems = []
            crtitemlist = []
            filename,filetype = QFileDialog.getOpenFileName(self,
                                                   "选择txt文件",
                                                   "d:/",
                                                   "All files (*);;Text file(*.txt)")
            self.dirpath.setText(filename)
            pathinfo = os.path.split(filename)
            print(pathinfo)
            with open(filename) as fp:
                for line in fp.readlines():
                    line = line.strip()
                    # print(line)
                    if line and not os.path.exists(pathinfo[0] + '/' + line):
                        crtitemlist.append(line)
                self.items = set(crtitemlist)
                print(self.items)
            if self.items:
                self.dirlist.addItems(self.items)
                newitems = ['md '+x for x in self.items]
                cmdstr = ' && '.join(newitems)
                cmdstr = 'cd ' + pathinfo[0] + ' && ' + cmdstr
                print(cmdstr)
                os.system(cmdstr)
                ms = "运行完成,自动化创建文件夹%s个,文件夹路径：%s" % (len(self.items),pathinfo[0])
                self.stbar.showMessage(ms)
                QMessageBox.about(self, "提示", ms)
            else:
                ms = "创建%s个文件夹，列表中文件均已存在,文件夹路径：%s" % (len(self.items), pathinfo[0])
                self.stbar.showMessage(ms)
                QMessageBox.about(self, "提示", ms)
        except Exception as e:
            QMessageBox.about(self,"提示","未能执行成功!\n\r错误代码：%s" % e.args)
            print("***********",e.args)


if  __name__ == "__main__":
    app = QApplication(sys.argv)
    rn = batAction()
    rn.show()
    sys.exit(app.exec_())