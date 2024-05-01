import cv2
import os 
from global_vars import STEP, START, VIDEO_FP

def extract_and_crop_frame(video_path, frame, crop_region, output_image_path):
    # Open the video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    frame_number = frame

    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture the frame.")
        return


    x, y, width, height = crop_region
    cropped_frame = frame[y:y+height, x:x+width]

    cv2.imwrite(output_image_path, cropped_frame)
    cap.release()
    cv2.destroyAllWindows()


def crop_frame_details(frame):
    video_path = VIDEO_FP
    crop_region = (570, 865, 125, 30)  # (x, y, width, height)
    # output_image_path = './frames/details/acropped_details_frame.png'
    output_image_path = f'./frames/details/cropped_details_frame{int((frame-START)/STEP)}.png'
    extract_and_crop_frame(video_path, frame, crop_region, output_image_path)

def crop_input_frame(frame):
    video_path = VIDEO_FP
    crop_region = (100, 235, 150, 30)  # (x, y, width, height)
    output_image_path = f'./frames/input/cropped_input_frame{int((frame-START)/STEP)}.png'
    extract_and_crop_frame(video_path, frame, crop_region, output_image_path)

def crop_counter_frame(frame):
    video_path = VIDEO_FP
    crop_region = (1285, 832, 55, 10)  # (x, y, width, height)
    output_image_path = f'./frames/counter/cropped_counter_frame{int((frame-START)/STEP)}.png'
    extract_and_crop_frame(video_path, frame, crop_region, output_image_path)

def crop_punish_frame(frame):
    video_path = VIDEO_FP
    crop_region = (1356, 830, 52, 14)  # (x, y, width, height)
    output_image_path = f'./frames/punish/cropped_punish_frame{int((frame-START)/STEP)}.png'
    extract_and_crop_frame(video_path, frame, crop_region, output_image_path)


# for i in range(0, 9800, 25):
#     crop_input_frame(i) 

# crop_punish_frame(2404)
# for i in range(START, 2484, 10):
#     crop_counter_frame(i)
# crop_input_frame(50)

# crop_frame_details(500)