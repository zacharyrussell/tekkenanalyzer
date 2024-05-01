import torch
from PIL import Image
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

model = None


def get_input_prediction(image_path):
    global model
    if model is None:
        model = torch.hub.load('ultralytics/yolov5', 'custom', path='./best.pt',force_reload=False, verbose=False)  # Update with the actual path
    img = Image.open(image_path)  
    results = model(img)
    result_df = results.pandas().xyxy[0]  

    if 'name' in result_df.columns:
        predictions = result_df['name'].unique() 
    
    return predictions



# fp = 'frames/input/cropped_input_frame218.png'
# get_input_prediction(fp)

