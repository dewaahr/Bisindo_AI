import threading
import time
from flask import Flask, Response
import torch
import cv2
import tkinter as tk

app = Flask(__name__)

model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')

def get_frames():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        for _, row in results.pandas().xyxy[0].iterrows():
            cv2.rectangle(frame, (int(row['xmin']), int(row['ymin'])), (int(row['xmax']), int(row['ymax'])), (255, 0, 0), 2)
            cv2.putText(frame, row['name'], (int(row['xmin']), int(row['ymin'])-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        labels = results.pandas().xyxy[0]['name'].tolist()
        label_text = ', '.join(labels)
        frame_height, frame_width = frame.shape[:2]
        text_size = cv2.getTextSize(label_text, cv2.FONT_HERSHEY_SIMPLEX, 0.9, 2)[0]
        text_x = (frame_width - text_size[0]) // 2
        text_y = frame_height - 10
        cv2.putText(frame, label_text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)  # Warna kuning (BGR: 0, 255, 255)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(get_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

def start_backend():
    app.run(host='0.0.0.0', port=5000)

def start_frontend():
    cap = cv2.VideoCapture("http://127.0.0.1:5000/video_feed")
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('YOLOv5 Object Detection', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()

def run_app():
    backend_thread = threading.Thread(target=start_backend, daemon=True)
    backend_thread.start()
    time.sleep(2)
    start_frontend()

def main():
    root = tk.Tk()
    root.title("Bisindo Transaltor")

    tk.Label(root, text="Bisindo Transaltor").pack(pady=10)
    tk.Button(root, text="Start Video Feed", command=run_app).pack(pady=10)
    tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()