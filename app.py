from flask import Flask,render_template,Response
import cv2

app = Flask(__name__)

camera = cv2.VideoCapture(-1)

def generateFrames():
    while True:
        success,frame = camera.read() ##returns 2 parameters boolean(if it is there menas) and the frame
        if not success:
            break;
        else:
            ans,buffer = cv2.imencode(".jpg",frame);
            frame = buffer.tobytes()
            # return should not be used 
            # because it will only read one time
            yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')#pass as hardcoded string

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/video')
def video():
   return Response(generateFrames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if "__name__" == "__main__":
    app.run(debug = True)