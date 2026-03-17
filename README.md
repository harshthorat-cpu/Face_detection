# Face Detection
This project implements a computer vision system capable of identifying and locating human faces within a digital image or a live video stream. By utilizing the OpenCV (Open Source Computer Vision Library), the system draws bounding boxes around detected faces in real-time, providing a foundation for tasks like facial recognition 

# Overview

This project implements face detection using OpenCV's Haar Cascade classifier, a machine learning-based approach that uses a cascade of simple features to detect faces efficiently. The application can process both static images and live webcam feeds.


# Features

+ Real-time face detection from webcam
+ Draws bounding boxes around detected faces
+ Lightweight and fast processing

---------
## Requirement

+ Python 3.X
+ opencv

-------------

## Installation


1. Clone the repository
```  

git clone [github.com](https://github.com/harshthorat-cpu/Face_detection.git)
cd Face_detection

```  

2. Create a virtual environment

```  

python -m venv venv
source venv/bin/activate
```  

3. Install dependencies

```  

pip install opencv-python

```  

### Run the file

```  

python face_detection.py
```  

## How it work's
The project uses OpenCV's pre-trained Haar Cascade classifier (haarcascade_frontalface_default.xml) to detect frontal faces. The cascade classifier works by:

+ Converting the image to grayscale
+ Scanning the image at multiple scales
+ Applying a series of simple feature detectors
+ Returning bounding box coordinates for detected faces




## Acknowledgement
+ [opencv.org](https://opencv.org/) for the computer vision library
+ Haar Cascade classifiers originally developed by Viola and Jones
