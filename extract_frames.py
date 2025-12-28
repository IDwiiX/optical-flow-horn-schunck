import cv2
import os

video_path = 'videotest.mp4'   
output_folder = 'frames'

os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)

frame_number = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break 

    frame_filename = os.path.join(output_folder, f'frame_{frame_number:04d}.jpg')
    cv2.imwrite(frame_filename, frame)

    frame_number += 1

cap.release()

print(f"Extracted {frame_number} frames to '{output_folder}' folder.")
