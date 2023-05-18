import moviepy.editor

# List of video file names
video_files = ['1.mp4','2.mp4','3.mp4','4.mp4','5.mp4','6.mp4','7.mp4','8.mp4','9.mp4','10.mp4','11.mp4','12.mp4','13.mp4','14.mp4','15.mp4','16.mp4','17.mp4','18.mp4','19.mp4','20.mp4']

for video_file in video_files:
    video = moviepy.editor.VideoFileClip(video_file)
    audio = video.audio
    audio_file = video_file.replace('.mp4', '.mp3')
    audio.write_audiofile(audio_file)
