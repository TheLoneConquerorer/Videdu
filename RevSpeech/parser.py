from pytube import YouTube
from ffmpy import FFmpeg

ytlink ='https://www.youtube.com/watch?v=NpPyLcQ2vdI'#'https://www.youtube.com/watch?v=rtlJoXxlSFE&list=PLyQSN7X0ro2314mKyUiOILaOC2hk6Pc3j'
yt = YouTube(ytlink)
title = yt.title.replace(".","").replace(":","")
yt.streams.filter(progressive=True,file_extension = "mp4").first().download(filename = title)
videoLink = title+".mp4"
print(videoLink)
audioLink = title+' audio.mp3'
ff=FFmpeg(
	inputs = {videoLink: None},
	outputs = {
		#yt.title+' video.mp4': ['-map', '0:0', '-c:a', 'copy', '-f', 'mp4'],
		audioLink : ['-y','-f','mp3','-ab','192000','-vn']
#		#['-filter','v','setpts',"0.5*PTS"]
	}
)

def cutAndPaste(times):
	ff = FFmpeg(
		inputs = {videoLink: None},
		outputs = {output.mp4: ['-t',times[0]]}
	)
	ff.run()
	ff = FFmpeg(
		inputs = {videoLink: None},
		outputs = {slow.mp4: ['-ss',times[0],'-t',times[1]]}
	)
	ff.run()
	ff = FFmpeg(
		inputs = {videoLink: None},
		outputs = {part3.mp4: ['-ss',times[1]]}
	)
	ff.run()
	ff = FFmpeg(
		inputs = {slow.mp4: None},
		outputs = {part2.mp4,["'-filter_complex","[0:v]setpts=0.5*PTS[v];[0:a]atempo=2.0[a]'","-map","'[v]'","-map","'[a]'"]}
	)
	ff.run()
	ff = FFmpeg(
		inputs = {"'part1.mp4 | part2.mp4 | part3.mp4'":None},
		outputs = {title + " edited.mp4": '-c copy'}
	)

ff.cmd
ff.run()

