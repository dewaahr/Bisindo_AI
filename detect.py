import cv2
import torch

# Load model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='bisndopt3.pt') # Ganti dengan model yang ingin digunakan

# Open camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = model(frame_rgb)
    results.render()

    for img in results.ims:
        frame_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        cv2.imshow('BISINDO Detection', frame_bgr)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
