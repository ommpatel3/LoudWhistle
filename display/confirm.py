import face_recognition

def check_identity():

    person_image = face_recognition.load_image_file("identity.png") #person saves

    id_image = face_recognition.load_image_file("id.png")#modi
    # print("loading complete---------")
    
    # remember to connect a function for screen shot id, then a function for webcam
    #then connect both functions as variables into the comparison function
    #then finally write code that allows connection to block chain file once requriments are satisfied
        

    try:
        person_face_encoding = face_recognition.face_encodings(person_image)[0]

        id_face_encoding = face_recognition.face_encodings(id_image)[0]
    except IndexError:
        print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
        quit()

    faceArray=[person_face_encoding]

    results = face_recognition.compare_faces(faceArray, id_face_encoding)

    print("Do the photos match? {}".format(results[0]))



#check_identity()

