import cv2
import numpy as np
import argparse
import os

def generate_events(video_path, threshold=30, output_file="events.txt"):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return
    
    ret, prev_frame = cap.read()
    if not ret:
        print("Error: Could not read first frame.")
        return
    
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    timestamp = 0
    
    with open(output_file, "w") as f:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            diff = gray.astype(np.int16) - prev_gray.astype(np.int16)
            
            event_indices = np.where(np.abs(diff) > threshold)
            for y, x in zip(*event_indices):
                polarity = 1 if diff[y, x] > 0 else -1
                f.write(f"{int(x)} {int(y)} {timestamp:.6f} {int(polarity)}\n")
            
            prev_gray = gray.copy()
            timestamp += 1 / cap.get(cv2.CAP_PROP_FPS)
    
    cap.release()
    print(f"Event data saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate synthetic event camera data from video.")
    parser.add_argument("video", help="Path to input video file.")
    parser.add_argument("--threshold", type=int, default=30, help="Intensity change threshold for event detection.")
    parser.add_argument("--output", default="events.txt", help="Output file for event data.")
    args = parser.parse_args()
    
    generate_events(args.video, args.threshold, args.output)
