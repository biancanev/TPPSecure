#!/usr/bin/python
"""
DevElec Main GUI

Author: Ryan Kwong
"""

#Import modules for use
import subprocess as sp
import socket
import os
import json
import sys#import the sys module for file operations
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


#Define main functions


#define the main window
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    with open('global_settings.json', 'r') as f:
      data = json.load(f)
      if data["license"] == "none":
        print("No applicable license found. Terminating process")
        os.system("pause")
      else:
        self.initUI()
    

  def initUI(self):
  	#set menubar items
    self.statusBar = QStatusBar()
    self.setStatusBar(self.statusBar)
    self.menubar = self.menuBar()
    self.runMenu = self.menubar.addMenu('&Run')
    self.viewMenu = self.menubar.addMenu('&View')
    self.setMenu = self.menubar.addMenu('&Settings')
	#buttons under run
    self.quickScan = QAction('Quick Scan', self)
    self.fullScan = QAction('Full Scan', self)
    self.secDiag = QAction('Security Diagnosis', self)
	#buttons under view
    self.sysInfo = QAction('System Info', self)
    self.reports = QAction('Reports', self)
    #buttons under settings
    self.globalSettings = QAction('Global', self)
    self.troubleshoot = QAction('Troubleshoot', self)
		#add menubar items
    self.runMenu.addAction(self.quickScan)
    self.runMenu.addAction(self.fullScan)
    self.runMenu.addAction(self.secDiag)
    self.viewMenu.addAction(self.sysInfo)
    self.viewMenu.addAction(self.reports)
    self.setMenu.addAction(self.globalSettings)
    self.setMenu.addAction(self.troubleshoot)
    self.title = QLabel("Computer Health:", self)
    self.title.setFont(QFont('Arial', 22))
    self.title.adjustSize()
    self.title.move(20, 40)
    #add Main menu screen
		#button functionality
    self.sysInfo.triggered.connect(lambda:self.sysInfoCom())
    self.quickScan.triggered.connect(lambda:quickScanCom())
    self.fullScan.triggered.connect(lambda:print("Worked"))
    self.showMaximized()
    self.setWindowTitle('TPPSecure 2021 [v.0.1.0]')
    self.show()
  
def quickScanCom():
  ip = socket.gethostbyname(socket.gethostname())
  MainWindow.title.setText("Computer Health for " + ip)
def sysInfoCom():
  pass
	

#Define main functions
def main():
  app = QApplication(sys.argv)
  ex = MainWindow()
  sys.exit(app.exec_())


if __name__ == '__main__':
  main()
  #try:
  #  main()
  #except:
  #  print(WindowsError)