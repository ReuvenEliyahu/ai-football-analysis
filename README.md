# AI Football Analysis ⚽

AI-based football video analysis with object tracking, camera mapping, and tactical visualizations.

## Project Overview

This repository contains a system for analyzing football matches from video. It uses deep learning and computer vision techniques to detect players and the ball, estimate camera movement frame-by-frame, and enable tactical insights through visualizations.

## Repository Structure

- `main.py` – Runs the full tracking and visualization pipeline
- `camera_movement_estimator/` – Camera motion estimation and utilities
- `trackers/` – Tracking logic and support functions
- `visualization/` – Annotating and plotting video frames
- `models/` – YOLOv8 model interface
- `utils/` – General utilities
- `data_loader/` – Helpers for loading input/output data
- `config/` – Configuration settings
- `data/` – Example input video and outputs

## Requirements

- Python 3.8+
- OpenCV
- Ultralytics YOLOv8
- NumPy
- Matplotlib

## Getting Started

1. Clone this repository
```bash
git clone https://github.com/[your-username]/ai-football-analysis.git
cd ai-football-analysis
```

2. Install dependencies (recommended to use a virtual environment)
```bash
pip install -r requirements.txt
```

3. Run the analysis
```bash
python main.py
```

## Features

- Object detection for players and ball
- Camera movement estimation
- Tactical frame-by-frame analysis
- Annotated visual outputs

## 🔗 Model Weights

This project uses a YOLOv8 model trained via [Roboflow](https://roboflow.com/) and Google Colab.  
The trained weights (`best.pt`) are not included in this repository due to file size limits.

You can:
- Train your own model using the Roboflow dataset + training notebook
- Or download pre-trained weights from your Roboflow project

To use your model, update the path in `yolo_interface.py`.

## Future Improvements

- Add real-time video stream support
- Improve multi-player tracking across frames
- Automate formation detection and heatmaps

## Acknowledgments

This project is based on [Abdullah Tarek’s Football Analysis](https://github.com/abdullahtarek/football_analysis).  
I used it as a learning guide and adapted parts of the code to run and debug it in my environment.

## Author

Reuven Eliyahu  
[LinkedIn](https://www.linkedin.com/)