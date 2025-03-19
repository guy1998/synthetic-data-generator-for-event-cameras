import cv2

width, height = int(max(x)) + 1, int(max(y)) + 1
fps = 30  # Adjust the frames per second as needed

# Create blank frames for event visualization
video_out = cv2.VideoWriter("event_output.avi", cv2.VideoWriter_fourcc(*"XVID"), fps, (width, height), False)

for t in np.unique(timestamps):
    frame = np.zeros((height, width), dtype=np.uint8)
    event_mask = timestamps == t
    frame[y[event_mask].astype(int), x[event_mask].astype(int)] = 255
    video_out.write(frame)

video_out.release()
print("Event video saved as event_output.avi")