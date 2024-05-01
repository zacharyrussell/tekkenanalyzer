import pandas as pd
# from moviepy.editor import VideoFileClip
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import moviepy
import numpy as np
from global_vars import *



def prep_video(frame, video_fp, move):
    fps = 60  

    start_frame = frame-60
    stop_frame = frame+60
    start_time = start_frame / fps
    stop_time = stop_frame / fps
    video = VideoFileClip(video_fp)

    # Clip the video between start_time and stop_time
    clipped_video = video.subclip(start_time, stop_time)

    slow_motion_video = clipped_video.fx(moviepy.video.fx.all.speedx, 0.5)
    # Write the result to a new video file
    txt_clip = TextClip(f'You used: "{move}"', fontsize=70, color='white', font='Arial', bg_color='black')
    txt_clip = txt_clip.set_position(('center', 'top')).set_duration(slow_motion_video.duration)
    
    # Overlay text 
    final_clip = CompositeVideoClip([slow_motion_video, txt_clip])
    return final_clip
    # final_clip.write_videofile('clipped_video.mp4', codec='libx264')











df = pd.read_csv("replay_data.csv")
total = len(df)
df.fillna(method='ffill', inplace=True)
na = df['possible_moves'].isna().sum()
print(total - na, '/', total)



def print_statistic(name, df):
    unique_counts = df[name].value_counts()
    print(unique_counts)


def generate_feedback(name):
    counters = df.loc[df[name] == 1]
    first_index = 0
    for index, row in counters.iterrows():
        if index - first_index >= 20:
            first_index = index
        else:
            df.loc[index, name] = 0
    counters = df.loc[df[name] == 1]

    countered_moves = counters[['possible_moves', 'frame']].values


    clips = []
    for detection in countered_moves:
        move = detection[0]
        frame = detection[1]
        clips.append(prep_video(frame, VIDEO_FP, move))

    final_clip = moviepy.editor.concatenate_videoclips(clips)

    final_clip.write_videofile(f'{name}_compiled_video2.mp4', codec='libx264')




generate_feedback('is_counter')
generate_feedback('is_punish')




# prep_video(2482, './kuma_replay_1.mp4', '1')