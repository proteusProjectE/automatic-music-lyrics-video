import requests
from bs4 import BeautifulSoup

#import custom modules
import whisperAlignment

def printLyrics(url, title,ytSongTitle,userFilePath):

	page = requests.get(url)
	html = BeautifulSoup(page.text, 'html.parser')
	[h.extract() for h in html('i')]
	lyrics = html.find('div').get_text(strip=True,separator='\n')

	#perform string analysis 1
	#find actual start and end lines of lyrics
	lines_analysis1 = lyrics.splitlines()
	i = 0
	beginning_line = 0
	end_line = 0
	line_to_detect_beginning = title + " Lyrics"
	for line in lines_analysis1:
		#if line is "song_title Lyrics", make the next line the starting line
		if line == line_to_detect_beginning:
			beginning_line=i+1
		#if line is "Embed", make the previous line the ending line
		if line == "Embed":
			end_line=i-1
		i+=1
	lines_analysis1 = lines_analysis1[beginning_line:end_line]

	#perform string analysis 2
	#remove any line containing "[" or "]"
	lines_analysis2 = []
	for line in lines_analysis1:
		if not ("[" in line) and not ("]" in line):
			lines_analysis2.append(line)

	#perform string analysis 3
	#remove ", " at the beginning of the line if it has it
	lines_analysis3 = []
	for line in lines_analysis2:
		line_to_add = line.removeprefix(', ')
		if line_to_add != ",":
			lines_analysis3.append(line_to_add)

	#perform string analysis 4
	#remove the following lines: 
	#"See ... Live"
	#Get tickets as low as..."
	#"You might also like"
	lines_analysis4 = []
	for line in lines_analysis3:
		#get the first few charcters in the line
		prefix = line[0:3]
		#get the last few characters in the line
		suffix = line[-4:]
		#prefix and suffix are needed only to check if the line != "See ... Live"
		if prefix!="See" and suffix!="Live":
			#check if the line does not begin with "Get tickets as low as"
			if line[0:21] != "Get tickets as low as":
				#check if line is equal to "You might also like"
				if line != "You might also like":
					#check if line equals "&" or ")" or "("
					if line!="&"and line!=")" and line!="(":
						lines_analysis4.append(line)

	#print lyrics
	final_lyrics = ''
	for line in lines_analysis4:
		print(line)
		final_lyrics=final_lyrics+line+'\n'

	whisperAlignment.align(final_lyrics,title,ytSongTitle,userFilePath)

	#now use whisper alignment to get srt file (which includes lyrics AND corresponding timestamps)


