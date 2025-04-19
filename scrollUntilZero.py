import pyautogui
from time import sleep

def scroll(j):
	pyautogui.keyDown('ctrl')
	i = 0
	while i < j:
		
		pyautogui.keyDown('left')
		sleep(0.01)
		pyautogui.keyUp('left')
		sleep(0.01)
		i+=1

	pyautogui.keyUp('ctrl')	