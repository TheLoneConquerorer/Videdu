from pytube import YouTube
from ffmpy import FFmpeg
import requests, json, time, os, string
ytlink ='https://www.youtube.com/watch?v=NpPyLcQ2vdI'#'https://www.youtube.com/watch?v=rtlJoXxlSFE&list=PLyQSN7X0ro2314mKyUiOILaOC2hk6Pc3j'
yt = YouTube(ytlink)
title = yt.title.replace(".","").replace(":","")
yt.streams.filter(progressive=True,file_extension = "mp4").first().download(filename = title)
videoLink = title+".mp4"
print(videoLink)
ff=FFmpeg(
	inputs = {videoLink: None},
	outputs = {
		#yt.title+' video.mp4': ['-map', '0:0', '-c:a', 'copy', '-f', 'mp4'],
		title+' audio.mp3': ['-y','-f','mp3','-ab','192000','-vn']
		#['-filter','v','setpts',"0.5*PTS"]
	}
)
ff.cmd
ff.run()
audioLink = title + ' audio.mp3'

aURL = "https://api.rev.ai/revspeech/v1beta/jobs"
headers = {
	'Authorization':'Bearer 013pWJnU_1foHRINs8J_mag71h_zBQPv6fi9MwrfXQSK34180d6W-FE3laPKTwYy9JQE_SITwR0cxUGmweTcbDVqA5kaM'
}
data = {
	'media_url' : ytlink,
	'metadata' : "Test"
}

r = requests.post(aURL,json = data,headers = headers)
id = r.json()['id']
print(id)
jURL = 'https://api.rev.ai/revspeech/v1beta/jobs/'+id
tURL = f'https://api.rev.ai/revspeech/v1beta/jobs/'+id+'/transcript'
#title + " transcript.json"
count = 0
while(r.json()["status"] != "transcribed" and r.json()["status"] != "failed"):
	r = requests.get(jURL, headers= headers)
	print("waiting" + str(count))
	count += 1
	print(r.json()["status"])
	time.sleep(10)
headers['Accept'] = 'application/vnd.rev.transcript.v1.0+json'
r = requests.get(tURL, headers= headers)
print(r.json())