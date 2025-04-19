#custom modules
import lyrics
import usingPyautogui
import ytVidTitle
import scrollUntilZero

#other modules
from time import sleep

#get user input
#ex yt: https://www.youtube.com/watch?v=idcamdI0g_o
#this yt video needs to contain the song (as its audio)
linkToYT = input("Enter the link to the YT video containing the song: ")
#ex lyrics: https://genius.com/Post-malone-staring-at-the-sun-lyrics
linkToGenius = input("Enter the link to the Genius lyrics: ")
#ex title: Staring at the Sun
actualSongTitle = input("Enter the title of the song (as it appears on Genius): ")
#ex filepath: C:\Users\User\Downloads
userFilePath = input("Enter the filepath to downloads (where the mp3 and srt file will be saved to): ")

#set variables
ytSongTitle = ytVidTitle.getTitle(linkToYT)
#srt file name
actualSongTitleSRT = actualSongTitle+".srt"

#actually start program
import ytmp3
ytmp3.type_vid_link(linkToYT)
ytmp3.start()
ytmp3.close()
ytSongTitle = ytSongTitle.rstrip() #remove empty character at the end
lyrics.printLyrics(linkToGenius,actualSongTitle,ytSongTitle,userFilePath)

import automateVideoEditor
automateVideoEditor.startVideoEditor(actualSongTitleSRT,userFilePath)
titleMP3 = ytSongTitle+".mp3" 
usingPyautogui.selectFileToUpload(titleMP3,userFilePath)
usingPyautogui.clickOnZoomOut()

#scroll until cursor is at 00:00:00, then add the music
continueFlag = True
while (continueFlag):
	current_time = automateVideoEditor.getCursorTime()
	if current_time == "00:00:00":
		continueFlag = False
	else:
		scrollUntilZero.scroll(50)
usingPyautogui.clickOnMusic()

#done
sleep(5)