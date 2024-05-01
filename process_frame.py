from advantage_extract import *

from global_vars import STEP, STOP, START, VIDEO_FP
from predict_input import *
from image_to_txt import *
from counter_punish_detect import *

import pandas as pd

def clean_and_save():
    df = pd.read_csv("kuma.csv",header = 1)
    df = df.drop(columns=['Notes', 'Tags', 'Image', 'Video'])
    df['Start up frame'] = df['Start up frame'].str.replace(',', '', regex=False).str.replace('i', '', regex=False).str.replace('~', '-', regex=False)
    df.to_csv('kuma_cleaned.csv', index=False)


def get_csv():
    df = pd.read_csv("kuma_cleaned.csv")
    return df

def narrow_possible_moves(image_path):
    df = get_csv()
    series = df.loc[df['Start up frame'] == get_attack_startup(image_path), 'Command']
    if series.empty:
        return "N/A"
    else:
        return series.iloc[0]


# print(narrow_possible_moves('./frames/details/cropped_details_frame136.png'))

def process_video_frames(video_fp):
    VIDEO_FP = video_fp
    
    data = []
    count = 0
    for i in range(START, STOP, STEP):
        if count % 50 == 0:
            print("At frame:", count)
        count +=1
        crop_counter_frame(i)
        crop_punish_frame(i)
        crop_input_frame(i)
        crop_frame_details(i)

        # Detect where counter and punishes happen
        file_number = int((i-START)/STEP)
        counter_fp = f'./frames/counter/cropped_counter_frame{file_number}.png'
        punish_fp = f'./frames/punish/cropped_punish_frame{file_number}.png'
        
        is_counter = is_orange(counter_fp, file_number) # 1 if true
        is_punish = is_orange(punish_fp, file_number) # 1 if true

        details_path = f'./frames/details/cropped_details_frame{file_number}.png' 
        possible_moves = narrow_possible_moves(details_path)

        input_fp = f'./frames/input/cropped_input_frame{file_number}.png'
        input_pred = get_input_prediction(input_fp)
        data.append([is_counter, is_punish, possible_moves, i])

    df = pd.DataFrame(data, columns=['is_counter', 'is_punish', 'possible_moves', 'frame'])
    df.to_csv('replay_data.csv', index=False)



process_video_frames('./kuma_replay_1.mp4')