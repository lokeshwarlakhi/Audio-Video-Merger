import os
from moviepy.editor import *


def combine_audio_video(audiofile, videofile, output_file_name_with_extension):
    download_path = os.getcwd()
    videoclip = VideoFileClip(videofile)
    audioclip = AudioFileClip(audiofile).subclip(24,31)
    video = videoclip.set_audio(audioclip)
    if not os.path.exists(f'{download_path}/output'): # if directory output dosen't
        os.makedirs(f'{download_path}/output')        # exist create it
    video.write_videofile(f'{download_path}/output/{output_file_name_with_extension}')
    while True: ### check if audio and video files are closed to delete them
        try:
            files = os.listdir(download_path)
            myfile = open(f'{download_path}/{files[1]}', "r+")
            myfile.close()
            os.remove(f'{download_path}/{audiofile}')
            os.remove(f'{download_path}/{videofile}')
            break                             
        except IOError:
            pass
combine_audio_video('test.mp3','test.mp4','lokidoki.mp4')