import cv2
import face_recognition

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
ds_factor=0.6

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        
        ###### previous code, facial detection only 
        success, image = self.video.read()
        image=cv2.resize(image,None,fx=ds_factor,fy=ds_factor,interpolation=cv2.INTER_AREA)
        gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        face_rects=face_cascade.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in face_rects:
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
            if cv2.waitKey(1)%256 == 32: #when spece is pressed, stop showing video
                break
        
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def check_identity(self):

        person_image = face_recognition.load_image_file("person.jpg") #akshay
        person2_image = face_recognition.load_image_file("person2.jpg")#modi

        id_image = face_recognition.load_image_file("id.jpeg")#modi
        # print("loading complete---------")

        try:
            person_face_encoding = face_recognition.face_encodings(person_image)[0]
            person2_face_encoding = face_recognition.face_encodings(person2_image)[0]

            id_face_encoding = face_recognition.face_encodings(id_image)[0]
        except IndexError:
            print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
            quit()

        faceArray=[person_face_encoding, person2_face_encoding]
        print("array created")

        results = face_recognition.compare_faces(faceArray, id_face_encoding)

        print("compare completed-----------")
        print("Is the unknown face a picture of akshay? {}".format(results[0]))
        print("Is the unknown face a picture of modi? {}".format(results[1]))
        
           