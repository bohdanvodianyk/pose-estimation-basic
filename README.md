# Pose Estimation using MediaPipe

This repository contains Python scripts for real-time pose estimation using the MediaPipe library and OpenCV. The project demonstrates the detection and tracking of human body landmarks in video streams.

## Project Structure

- **PoseEstimationMin.py**: A minimal script that captures video (either from a file or webcam), processes it to detect human body landmarks, and displays the results.
- **PoseEstimationModule.py**: Defines a `poseDetector` class that encapsulates the pose detection functionality. This script includes additional features and customizability, and demonstrates the use of the `poseDetector` class with a video file.

## Features

- **Real-Time pose detection**: detects human body landmarks in real-time from video feeds.
- **Customizable parameters**: offers customization for the pose detection model, including model complexity, smoothness, and confidence thresholds.

## Getting Started

### Prerequisites

- Python 3.x
- OpenCV
- MediaPipe

### Installation

1. Clone the repository.
2. Install required libraries:
`pip install opencv-python mediapipe`

### Usage

- To run the minimal pose estimation:
`python PoseEstimationMin.py`
- To use the pose detection with the `poseDetector` class:
`python PoseEstimationModule.py`
(The work of each script is equal)


## Acknowledgements

- This project uses the [MediaPipe](https://google.github.io/mediapipe/) framework for pose detection.
- The test videos could be download from [Pexels](https://www.pexels.com/videos/).

## Contact

For any queries or feedback, please raise an issue in the repository.

