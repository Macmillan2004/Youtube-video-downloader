l = ['128kbps','50kbps','70kbps','160kbps']
url = input("Enter the URL of the YT Video You Need to Download\n")
c = int(input("Enter Video or Audio Option 1 for Video and 2 for audio\n 1.Video\n 2.Audio\n"))
from pytube import YouTube

if(c==1):
    a=input("Enter the Resolution of Video in Pixels...like 240p or 360p or 480p or 720p....\n")
    youtube = YouTube(url)
    video = youtube.streams.filter(file_extension='mp4',resolution=a).first()
    video.download()
    print('Video Downloaded Successfully\nVideo is saved same location of this file')
elif(c==2):
    b=int(input("Enter Quality Option 1(or)2(or)3....\n 1.128kbps\n 2.50kbps\n 3.70kbps\n 4.160kbps\n"))
    if(b>4):
        print("Audio Download Fail")
        exit
    else:
        youtube = YouTube(url)
        audio = youtube.streams.filter(only_audio=True,abr=l[b-1]).last()
        audio.download()
        print('Audio Downloaded Successfully\nVideo is saved same location of this file')
else:
    print("Download Fail,Please Try again")