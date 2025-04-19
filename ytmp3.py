from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui
from selenium.common.exceptions import NoSuchElementException

#keeps browser open when finished
options = Options()
#options.add_experimental_option("detach",True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
    options=options)
#driver = webdriver.Chrome(service = chromedriver, options=options)

#go to website
driver.get("https://y2mate.nu/en-Abbs/")
#maximize window
#driver.maximize_window()

def type_vid_link(link):
    sleep(2)
    pyautogui.typewrite(link)
    sleep(1)

def start():
    convert = driver.find_element(By.XPATH,"/html/body/form/div[2]/button[2]")
    convert.click()
    sleep(2)
    flag = True
    while flag:
        try:
            download = driver.find_element(By.XPATH,"/html/body/form/div[2]/button[1]")
            download.click()
            flag = False
        except NoSuchElementException:
            pass
        sleep(1)
    sleep(10)

def close():
    driver.quit()
