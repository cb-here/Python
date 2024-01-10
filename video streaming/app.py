from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

camera = cv2.VideoCapture(0) # using primary camera

def generate_frames():
    while True:
        # reading the frame
        success, frame = camera.read()
        if not success:
            break
        else:
            # encoding frame into .jpg format
            ret, buffer = cv2.imencode('.jpg',frame)
            if not ret:
                break
            else:
                frame = buffer.tobytes()
        yield(b'--frame\r\n'
        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
@app.route("/")
@app.route("/home")
def home():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)