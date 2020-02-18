# dli_image_regression

NVIDIA IoT [Deep Learning Institute](https://www.nvidia.com/en-us/deep-learning-ai/education/) image regression at the edge (IoT) project for Jetson Nano. 

This project is meant to be run at the edge on an NVIDIA Jetson Nano (or similar ARM IoT architecture computer).  

## Requirements
* Jupyter Notebooks (AKA IPython)
* Pytorch
* Jetpack SDK or [DLI Jetson Nano image](https://developer.download.nvidia.com/training/nano/ainano_v1-1-1_20GB_200203B.zip) (preferably the latter for headless mode compatibility)
* [Jetcam](https://github.com/NVIDIA-AI-IOT/jetcam)
* [Jupyter Clickable Image Widget](https://github.com/jaybdub/jupyter_clickable_image_widget)

## Repository structure ##

### [data](data) 
Contains 360 images times 3 classes (total images = 1080) taken and used for training. The images were encrypted for privacy purposes.

### [models](models) 
Contains different model iterations and are named after the total training images and epochs. The best performing model is the *xy_360dpx3_45ep.pth* model which was trained with 200 images per class and for a total of 35 epochs.

### [notebooks](notebooks)
Contains the Jupyter notebook used to interactively train and evaluate an emotion prediction (up or down) model using deep learning and PyTorch.

### [src](src)
Standard src scripts and utilities plus a folder structure generator script.

## Usage
Use the interactive notebook from the notebooks folder and train your own model or load one already made from the models folder and evaluate how effective it is using your camera. The model will output xy coordinates (in the form of a circle) where it thinks it found the selected face feature class (only one at a time).

## License
[MIT License](https://github.com/socd06/dli_emotions/blob/master/LICENSE)
