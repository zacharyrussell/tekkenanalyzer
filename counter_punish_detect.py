import cv2
import numpy as np
from global_vars import STEP
# Load your image

def get_avg_color(filepath):
    img = cv2.imread(filepath)
    # Convert image to RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Calculate the average color of the entire image
    average_color = np.mean(img_rgb, axis=(0, 1))
    return average_color


def is_orange(filepath, frame):

    average_color = get_avg_color(filepath)

    orange = np.array([130, 55, 72]) 
    grey = np.array([57, 55, 72])  
    red = np.array([94, 57, 63]) 

    distance_to_orange = np.linalg.norm(orange - average_color)
    distance_to_red = np.linalg.norm(red - average_color)
    distance_to_grey = np.linalg.norm(grey - average_color)

    if distance_to_orange < distance_to_grey:

        
        if('counter' in filepath):
            if(average_color.sum()> get_avg_color(f'frames/punish/cropped_punish_frame{frame}.png').sum()):
                return 1
            else:
                return 0
        else:
            if(average_color.sum() > get_avg_color(f'frames/counter/cropped_counter_frame{frame}.png').sum()):
                return 1
            else:
                return 0
        # return 1
    else:
        # print("The average color of the image is closer to grey.")
        return 0

    print(f"The average color of the image is: {average_color}")

# stays lit for around 48 frames
# count = 0
# for i in range(222, 2484, 10):
#     path = f'frames\punish\cropped_punish_frame{int((i-222)/10)}.png'
#     orange = is_orange(path, int((i-222)/STEP))
#     count += orange

# count = 0
# for i in range(222, 2484, 10):
#     path = f'frames\counter\cropped_counter_frame{int((i-222)/10)}.png'
#     orange = is_orange(path, int((i-222)/STEP))
#     count += orange


