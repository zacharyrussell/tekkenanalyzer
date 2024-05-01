import os

def train_yolov5():
    # Define paths and parameters
    data_yaml = 'data.yaml'  # Path to your dataset YAML
    weights_path = 'yolov5s.pt'  # Use pre-trained weights for transfer learning
    img_size = 150  # Image size
    batch_size = 16  # Batch size, may need to reduce if memory issues occur
    epochs = 3  # Number of epochs to train

    # Ensure CUDA is not used
    os.environ['CUDA_VISIBLE_DEVICES'] = '-1'  # This line disables GPU

    # Command to run training
    train_cmd = f"python ./yolov5/train.py --img {img_size} --batch {batch_size} --epochs {epochs} --data {data_yaml} --weights {weights_path}"
    os.system(train_cmd)

if __name__ == '__main__':
    train_yolov5()
