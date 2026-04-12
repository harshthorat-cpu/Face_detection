# Face Detection & Blurring

This project implements a computer vision system capable of identifying, locating, and blurring human faces within a digital image or a live video stream. By utilizing the OpenCV (Open Source Computer Vision Library), the system detects faces and applies blur effects in real-time, providing a foundation for privacy protection and facial anonymization tasks.

# Overview

This project implements face detection using OpenCV's Haar Cascade classifier, a machine learning-based approach that uses a cascade of simple features to detect faces efficiently. Once faces are detected, the application can apply Gaussian blur or pixelation effects to protect privacy. The application can process both static images and live webcam feeds.


# Features

+ Real-time face detection from webcam
+ Face blurring with multiple blur techniques (Gaussian blur, pixelation)
+ Draws bounding boxes around detected faces
+ Lightweight and fast processing
+ Privacy-preserving face anonymization
+ Supports both static images and live video streams

---------
## Requirements

+ Python 3.X
+ opencv-python

-------------

## Installation

1. Clone the repository

```bash
git clone https://github.com/harshthorat-cpu/Face_detection.git
cd Face_detection
```

2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies

```bash
pip install opencv-python
```

## Run the file

```bash
python face_detection.py
```

## How it Works

### Face Detection
The project uses OpenCV's pre-trained Haar Cascade classifier (haarcascade_frontalface_default.xml) to detect frontal faces. The cascade classifier works by:

+ Converting the image to grayscale
+ Scanning the image at multiple scales
+ Applying a series of simple feature detectors
+ Returning bounding box coordinates for detected faces

### Face Blurring
Once faces are detected, the application applies blur effects to anonymize them:

+ **Gaussian Blur**: Applies a Gaussian blur kernel to the detected face region for smooth blurring
+ **Pixelation**: Reduces the resolution of the detected face region for a pixelated effect
+ Blur intensity can be customized based on privacy requirements
+ Real-time processing ensures minimal performance impact

## Usage

### Basic Face Detection
The system automatically detects faces in the video stream and can draw bounding boxes around them.

### Face Blurring
Enable face blurring to automatically blur detected faces in real-time, useful for:
- Privacy protection
- Video anonymization
- Compliance with privacy regulations
- Masking sensitive information

## Acknowledgements

+ [opencv.org](https://opencv.org/) for the computer vision library
+ Haar Cascade classifiers originally developed by Viola and Jones
