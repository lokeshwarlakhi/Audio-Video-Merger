
from moviepy.editor import *

def combine_audio_video(audiofile, videofile, output_file_name_with_extension):
    download_path = os.getcwd()
    videoclip = VideoFileClip(videofile)
    audioclip = AudioFileClip(audiofile)
    video = videoclip.set_audio(audioclip)
    if not os.path.exists(f'{download_path}/output'):
        os.makedirs(f'{download_path}/output')        
    video.write_videofile(f'{download_path}/output/{output_file_name_with_extension}')
    video.close()
    while True: ### check if audio and video files are closed to delete them
        try:
            os.remove(f'{download_path}/{audiofile}')
            os.remove(f'{download_path}/{videofile}')
            break                             
        except IOError:
            break

dir = os.getcwd()
audio_dir = os.listdir(f'{dir}/audio')
video_dir = os.listdir(f'{dir}/video')

audio_dir[0],video_dir[0]
j=0
for i in audio_dir:
    combine_audio_video(f'{dir}/audio/{i}',f'{dir}/video/{video_dir[j]}',video_dir[j])
    j+=1




