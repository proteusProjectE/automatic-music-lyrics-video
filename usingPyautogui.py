import pyautogui
from time import sleep

def selectFileToUpload(filename, userFilePath):
	sleep(2)
	filepath = userFilePath + "\\" + filename + "\n" 
	#\n is Enter to finalize file selection
	pyautogui.typewrite(filepath)

def clickOnMusic():
	#click on music to add to timeline
	sleep(2)
	pos_of_img = pyautogui.locateOnScreen('musicButton.png',confidence=0.7)
	#find center of img
	x = (pos_of_img[0]*2+pos_of_img[2])/2
	y = (pos_of_img[1]*2+pos_of_img[3])/2
	pyautogui.click(x,y)

def clickOnZoomOut():
	sleep(2)
	pos_of_img = pyautogui.locateOnScreen('zoomOut.png',confidence=0.7)
	#find center of img
	x = (pos_of_img[0]*2+pos_of_img[2])/2
	y = (pos_of_img[1]*2+pos_of_img[3])/2
	pyautogui.click(x,y)

def clickOnOK():
	sleep(2)
	pos_of_img = pyautogui.locateOnScreen('okButton.png',confidence=0.7)
	#find center of img
	x = (pos_of_img[0]*2+pos_of_img[2])/2
	y = (pos_of_img[1]*2+pos_of_img[3])/2
	pyautogui.click(x,y)