import numpy as np
from PIL import Image
import os



print("starting\n")


#constants

epochs = 400   #Number of epochs you want to train the network
alpha = 0.00001#Learning rate for the training process

width=1280 #Width of the picture you are working with
height=720 #Heigth of the picture you are working with

color1=[255,255,255]   #Output color for the category "color"
color0=[0,0,0]         #Output color for the category "other"

# Set the seed for reproducibility

np.random.seed(123456)
input_image_path = 'training.jpg'
label_image_path = 'training_label.jpg'


print("Current working directory:", os.getcwd())

# Absolute paths to the images
input_image_path = "/home/petrarka/Desktop/NN_RGB_FPGA/training.jpg"
label_image_path = "/home/petrarka/Desktop/NN_RGB_FPGA/training_label.jpg"

# Open the images
input_picture = Image.open(input_image_path)
label_picture = Image.open(label_image_path)

# Convert images to numpy arrays
input_picture_np = np.array(input_picture)
label_picture_np = np.array(label_picture)

# Print the numpy array of the input picture
print(input_picture_np)