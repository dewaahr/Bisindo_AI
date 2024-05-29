from flask import Flask, render_template, Response, jsonify
import cv2
import torch

app = Flask(__name__)

model = torch.hub.load('ultralytics/yolov5', 'custom', path='bisndopt3.pt') #Ganti dengan Model yang ingin dipakai
cap = None

def gen_frames():
    global cap
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        else:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = model(frame_rgb)
            results.render()
            for img in results.ims:
                frame_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
                ret, buffer = cv2.imencode('.jpg', frame_bgr)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('app.html')

@app.route('/video_feed')
def video_feed():
    global cap
    if cap is not None and cap.isOpened():
        return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
    else:
        return Response(b'')

@app.route('/start_camera', methods=['POST'])
def start_camera():
    global cap
    if cap is None or not cap.isOpened():
        cap = cv2.VideoCapture(0)
    return jsonify({'status': 'Camera started'})

@app.route('/stop_camera', methods=['POST'])
def stop_camera():
    global cap
    if cap is not None and cap.isOpened():
        cap.release()
    return jsonify({'status': 'Camera stopped'})

if __name__ == '__main__':
    app.run(debug=True)
