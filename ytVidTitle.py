from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def getTitle(video_url):

	# Initialize the WebDriver (Make sure you have chromedriver installed)
	driver = webdriver.Chrome()

	# Open YouTube video
	#video_url = "https://www.youtube.com/watch?v=swDam6Hrsm8"  # Example URL
	driver.get(video_url)

	# Wait for page to load (optional but recommended)
	time.sleep(3)

	# Get video title using the title tag
	title = driver.title
	title = title.replace("- YouTube","")

	# Close browser
	driver.quit()

	return title

