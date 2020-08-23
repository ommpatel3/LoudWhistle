from flask import Flask, render_template, Response, request
from camera import VideoCamera
import cv2
import confirm

app = Flask(__name__)

@app.route('/', methods= ['GET','POST'])
def index():
    return render_template('index.html')

screenshot=False

def gen(camera):
    while screenshot==False:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')



def contact():
    if request.method == 'POST':
        if request.form.get['Take Photo'] == 'Take Photo':
            screenshot = True
    elif request.method == 'GET':
        print("Button was pressed")
    return render_template('index.html', form=form)

def comparison():
    if request.method == 'POST':
        if request.form.get['Verify'] == 'Verify':
            print("pressed verify")
            #confirm.check_identity()
    elif request.method == 'GET':
        print("Button was pressed")
    #return render_template('index.html', form=form)



# def comparison(): 
#     if request.method == 'POST':
#         if request.form.get['Verify'] == 'Verify':
#             print(' I stopped here! ')
#             confirm.check_identity()
#     elif request.method == 'GET':
#         print("Button was pressed")
#     return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)