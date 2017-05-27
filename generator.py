#!/usr/bin/python
# -*- coding: utf-8 -*-

# absolute.py

import sys, os
from PyQt4 import QtGui, QtCore
import random


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        label1 = QtGui.QLabel('About this application:', self)
        label1.move(15, 10)

        label2 = QtGui.QLabel('Generate random items from the given file.', self)
        label2.move(15, 30)

        # window
        self.setWindowTitle('Random Generate')
        self.resize(280, 300)
        
        # Open file
        openFile = QtGui.QPushButton('Select file', self)
        openFile.setGeometry(10, 10, 100, 30)
        openFile.move(50, 80)
        self.connect(openFile, QtCore.SIGNAL('clicked()'), self.showDialog)
        
        # total input
        total_tip = QtGui.QLabel('Total:', self)
        total_tip.move(50, 130)

        self.label_total = QtGui.QLineEdit(self)
        self.label_total.move(100, 130)
        
        # select number input
        select_tip = QtGui.QLabel('Select:', self)
        select_tip.move(50, 170)

        self.label_select = QtGui.QLineEdit(self)
        self.label_select.move(100, 170)

        # generate
        ok = QtGui.QPushButton('Generate', self)
        ok.setGeometry(10, 10, 60 ,30)
        ok.move(50, 210)

        self.connect(ok, QtCore.SIGNAL('clicked()'),
                     self.submmit)

        # close
        quit = QtGui.QPushButton('Close', self)
        quit.setGeometry(10, 10, 60 ,30)
        quit.move(150,210)
        
        self.connect(quit, QtCore.SIGNAL('clicked()'),
                     self.close)

        # test button, only for debug.
#        t = QtGui.QPushButton('Test', self)
#        t.setGeometry(10, 10, 60 ,30)
#        t.move(50,250)
        
#        self.connect(t, QtCore.SIGNAL('clicked()'),
#                     self.testfunc)


    def submmit(self):
        total = self.label_total.text()
        select = self.label_select.text()
        a = range(1,int(total)+1)
        b = int(select)
        ran_list = random.sample(a,b)
        print ran_list
        new_name=0
        filepath = os.path.split(str(self.filename))[0]+'/'
        while os.path.exists("%s%s.txt"%(filepath, new_name)):
            new_name = new_name+1
        w = open("%s%s.txt"%(filepath, new_name),"a")
        with open(self.filename, 'r') as f:
            content = f.read()
            
            new_num = 0
            for num in ran_list:
                num_tag_a = '%s%s'%('\n', num)
                num_tag_b = '%s%s'%('\n', num+1)
                if num == 1:
                    num_content = '%s%s'%('\n', content[:content.index(num_tag_b)])
                elif num == int(total):
                    num_content = content[content.index(num_tag_a):]
                else :
                    num_content = content[content.index(num_tag_a):content.index(num_tag_b)]
                new_num = new_num + 1
                new_content = '%s%s%s'%('\n', new_num, num_content[len(num_tag_a):])
                w.write(new_content)
        w.close()


#        f = open(self.filename, 'r')
#        print ran_list

        # e='%s%s'%('\n',d+1)
        # c=b[b.index('\n3'):b.index('\n4')]
        # 

    def showDialog(self):
        self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File',
                                                     '/home')
        print(self.filename)
#        print(os.path.split(str(self.filename))[0])

    def testfunc(self):
        print(self.filename)


app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())
