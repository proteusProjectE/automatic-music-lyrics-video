import stable_whisper

#https://github.com/jianfch/stable-ts

def align(text,actualSongTitle,ytSongTitle,userFilePath):
	model = stable_whisper.load_model('base')
	print("finished loading model")
	#filepath of song to align to
	filepathToAlignTo = userFilePath + "\\" + ytSongTitle+".mp3"
	result = model.align(filepathToAlignTo, text, language = 'en', original_split=True)
	#file path to save to
	filepathToSaveTo = userFilePath + "\\" + actualSongTitle+".srt"
	result.to_srt_vtt(filepathToSaveTo,word_level=False)