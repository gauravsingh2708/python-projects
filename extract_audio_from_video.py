import moviepy.editor as me
video=me.VideoFileClip('/Users/gaurav/Desktop/python projects/Movie on 05-02-1941 Saka at 12.06 AM.mov')
audio=video.audio
audio.write_audiofile('result.mp3')