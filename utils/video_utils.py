import cv2
import os

def read_video(video_path):
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")
    
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError(f"Could not open video file: {video_path}")
    
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    
    cap.release()
    if not frames:
        raise ValueError("No frames were read from the video")
    
    return frames

def save_video(output_video_frames, output_video_path):
    if not output_video_frames:
        raise ValueError("No frames to save")
    
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_video_path), exist_ok=True)
    
    # Get frame dimensions from the first frame
    height, width = output_video_frames[0].shape[:2]
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, 24, (width, height))
    
    if not out.isOpened():
        raise ValueError(f"Could not create video writer for: {output_video_path}")
    
    for frame in output_video_frames:
        out.write(frame)
    
    out.release()