from keras.models import load_model
import cv2 
import numpy as np
import time

np.set_printoptions(suppress=True)

model = load_model("keras_Model.h5", compile=False)
class_names = open("labels.txt", "r").readlines()

camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = camera.read()
    if not ret:
        break

    input_image = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
    input_image = np.asarray(input_image, dtype=np.float32).reshape(1, 224, 224, 3)
    input_image = (input_image / 127.5) - 1

    prediction = model.predict(input_image)
    index = np.argmax(prediction)
    class_name = class_names[index].strip()
    confidence_score = prediction[0][index]

    text = f"Class: {class_name} | Confidence: {confidence_score * 100:.2f}%"
    cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow("Webcam Image", frame)

    keyboard_input = cv2.waitKey(1)
    if keyboard_input == 27:
        break

    # time.sleep(3)

camera.release()
cv2.destroyAllWindows()
