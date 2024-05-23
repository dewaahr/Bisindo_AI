import threading
import time
import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import torch
import cv2
from flask import Flask, Response

app = Flask(__name__)

model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')

def get_frames():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)

        labels = results.pandas().xyxy[0]['name'].tolist()
        label_text = ', '.join(labels)
        frame_height, frame_width = frame.shape[:2]
        text_size = cv2.getTextSize(label_text, cv2.FONT_HERSHEY_SIMPLEX, 0.9, 2)[0]
        text_x = (frame_width - text_size[0]) // 2
        text_y = frame_height - 10
        cv2.putText(frame, label_text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(get_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

def start_backend():
    app.run(host='0.0.0.0', port=5000)

def update_frame(label):
    cap = cv2.VideoCapture("http://127.0.0.1:5000/video_feed")
    while True:
        ret, frame = cap.read()
        if ret:
            cv2_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2_image)
            imgtk = ImageTk.PhotoImage(image=img)
            label.imgtk = imgtk
            label.configure(image=imgtk)
        time.sleep(0.03)

def run_app():
    backend_thread = threading.Thread(target=start_backend, daemon=True)
    backend_thread.start()

    time.sleep(2)  # Beri waktu untuk backend Flask mulai

    root = tk.Tk()
    root.title("YOLOv5 Object Detection")

    label = Label(root)
    label.pack()

    video_thread = threading.Thread(target=update_frame, args=(label,), daemon=True)
    video_thread.start()

    root.mainloop()

if __name__ == "__main__":
    run_app()
