from pytubefix import YouTube

url = input("Gib einen Youtube Link ein: ")

youtube_format = input("Welches Format möchtest du haben ? (audio/video): ")

if youtube_format.lower() == "video":
    print("Video wird heruntergeladen..")
    YouTube(url).streams.get_highest_resolution().download("/Users/suheibmarzouka/Desktop/24-01-ON/Workspaces/python-24-11/1106/Youtube Videos")
    print("Video wurde erfolgreich heruntergeladen")

elif youtube_format.lower() == "audio":
    print("Audio wird heruntergeladen..")
    YouTube(url).streams.get_audio_only().download("/Users/suheibmarzouka/Desktop/24-01-ON/Workspaces/python-24-11/1106/Youtube Audios")
    print("Audio wurde erfolgreich heruntergeladen")

else:
    print("Erlaubte Eingaben sind nur 'audio' oder 'video'")