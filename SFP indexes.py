import sys
import time
import datetime
import os
import csv
import webbrowser
import random
import re
import math
import string

################################################### Ahmed Elaraby ####################################################
######################################################################################################################




####################################################################################################
#################################### MAIN ##########################################################

def Main():

	objTab = crt.GetScriptTab()
	objConfig = objTab.Session.Config;

	objTab.Screen.Synchronous = True
	objTab.Screen.IgnoreEscape = True

	strValue = objConfig.GetOption("Keymap")
	value1 = strValue[0]
	value2 = strValue[1]
	x1 = value1.split('"')
	x2 = value2.split('"')
	
	user = x1[1]
	pass1 = x2[1]

	SourceHost = crt.Dialog.Prompt( "Please Enter Source Host Name","Ahmed Elaraby")

	crt.Screen.Send(SourceHost + "\r")
	
	cmx = crt.Screen.WaitForStrings(['login:','Username:','~]$'],5)

	if cmx == 1:
		crt.Screen.Send(user+"\r")
		crt.Screen.WaitForString("Password:")
		crt.Screen.Send(pass1+"\r")
		#RouterType = crt.Screen.WaitForStrings(['J-','Username:','~]$'],5)
		crt.Screen.WaitForString("EG>")
		crt.Screen.Send("start shell pfe network afeb0\r")
		crt.Screen.WaitForString(")#")
		crt.Screen.Send("show sfp list\r")
		crt.Screen.WaitForString("I2C Acceleration")

		Rows = []
		PortRow = crt.Screen.CurrentRow - 2
		readPortRow = crt.Screen.Get(PortRow, 1,PortRow,200).strip()
		Rows.append(readPortRow)

		#crt.Dialog.MessageBox(readPortRow)

		while readPortRow.startswith("--") == False:
			PortRow = PortRow - 1
			readPortRow = crt.Screen.Get(PortRow, 1,PortRow,200).strip()
			Rows.append(readPortRow)

		SFPindex = []
		for i in range (0, len(Rows)):
			
			RowPortArr = Rows[i].split(" ")
			RowPort = RowPortArr[0]
			if RowPort.isdigit() == True:
				SFPindex.append(RowPort)

		crt.Screen.WaitForString(")#")
		for i in range (0, len(SFPindex)):
			crt.Screen.Send("show sfp "+SFPindex[i]+"\r")
			crt.Screen.WaitForString(")#")
			crt.Screen.Send("show sfp "+SFPindex[i]+" info\r")
			crt.Screen.WaitForString(")#")

	if cmx == 2:
		crt.Screen.Send(user+"\r")
		crt.Screen.WaitForString("Password:")
		crt.Screen.Send(pass1+"\r")
	
	if cmx == 3:
		crt.Dialog.MessageBox("Can't access Router!","Ahmed Elaraby")

	

Main()
