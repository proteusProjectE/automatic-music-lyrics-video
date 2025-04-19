from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait

#import custom module
import usingPyautogui

#keeps browser open when finished
options = Options()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
	options=options)
#driver = webdriver.Chrome(service = chromedriver, options=options)

#go to website
driver.get("https://www.capcut.com/editor?enter_from=page_header&current_page=landing_page&from_page=landing_page")
#maximize window
#driver.maximize_window()

def uploadSrtFile(srtFileName,userFilePath):

	#select caption menu
	sleep(2)
	captionButton = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div[6]/div[1]")
	captionButton.click()

	#select upload srt button
	sleep(2)
	uploadSrtButton = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[3]/header/div[2]")
	uploadSrtButton.click()

	#select srt file to upload
	usingPyautogui.selectFileToUpload(srtFileName, userFilePath)

def startVideoEditor(srtFileName,userFilePath):

	sleep(2)
	exitOutOfSignInButton = driver.find_element(By.CLASS_NAME, "lv_sign_in_panel_wide-close")
	exitOutOfSignInButton.click()

	#click OK
	usingPyautogui.clickOnOK()

	#accept cookies if they show up
	try:
		sleep(2)
		acceptCookies = driver.find_element(By.XPATH, "/html/body/div[9]/div/div/div/button[2]")
		acceptCookies.click()
	except:
		pass

	# click OK again
	usingPyautogui.clickOnOK()

	# click OK again
	usingPyautogui.clickOnOK()

	#upload srt file
	uploadSrtFile(srtFileName,userFilePath)

	#click on media button
	sleep(4)
	mediaButton = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div[1]/div[1]")
	mediaButton.click()

	#upload 
	sleep(2)
	uploadMedia = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div/button")
	uploadMedia.click()

	#upload file
	sleep(2)
	uploadFile = driver.find_element(By.XPATH,"/html/body/div[17]/span/div/div/div[1]/div")
	uploadFile.click()

def getCursorTime():
	sleep(2)
	cursor = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/span[1]")
	print(cursor.text)
	return cursor.text


