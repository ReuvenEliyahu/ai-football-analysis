# AI Football Analysis ⚽

AI-based football video analysis with object tracking, camera mapping, and tactical visualizations.

## Project Overview

This repository contains a system for analyzing football matches from video. It uses computer vision techniques to detect players and the ball, estimate camera movement, and generate visual insights for tactical analysis.

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

- Player and ball detection using computer vision
- Camera movement estimation
- Player and team tracking
- Tactical video annotations and plots

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