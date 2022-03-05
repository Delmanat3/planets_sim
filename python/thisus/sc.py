import cv2
import time
import datetime


cap = cv2.VideoCapture(1)

# requires greyscale image type for input

face = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

body = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_fullbody.xml")


recording = False
detection_stopped_time = None
timer = False
sec_rec = 5


# cap3 is int val of width, 4 the height

frame_size = (int(cap.get(3)), int(cap.get(4))) #size of the video width, height
fourcc = cv2.VideoWriter_fourcc(*"mp4v")#getting code for the file format


while True:
    ret, frame = cap.read() #capture frame

    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#convert to greyscale

    # scale fact= num that determines accuracy anf speed. 1.1-1.5 1.3 is optimal.  min is 1 the lower the scale the heigher accureacy

    faces = face.detectMultiScale(grey, 1.3, 5)#pass in grey vid for face processing

    # decides how many times it goes over the targets. not picking up go lower picking up to many go heigher
    # pass the grey image scale factor and min number of neighbors returns list of faces with x,y

    # scale fact= num that determines accuracy anf speed. 1.1-1.5 1.3 is optimal.  min is 1 the lower the scale the heigher accureacy

    bodies = body.detectMultiScale(grey, 1.3, 5)#pass in grey for body detection

    if len(faces) + len(bodies) > 0: #if anything
        if recording: #are we currently recording
            timer = False #if timer was about to end reset it
        else:
            recording = True #if face or body detected start
            current_time = datetime.datetime.now().strftime("%d-%M-%Y-%H-%S")#current time
            # output stream: filename, fourcharecter code, frame rate, framesize
            out = cv2.VideoWriter(
                f"{current_time}.mp4", fourcc, 20, frame_size) #output stream
            print("recording started")
    elif recording: # start the process
        if timer: # if 
            if time.time()-detection_stopped_time >= sec_rec: #see if timer expires
                recording: False
                timer = False
                out.release()
                print("recording stopped")
        else:
            timer = True #if the timer is not expired continue
            detection_stopped_time = time.time()
   
   
    if recording:
        out.write(frame)#rite to the screen

    for (x, y, width, height) in faces:
        # pass in two corners of rectangle to extrap and pass color
        cv2.rectangle(frame, (x, y), (x+width, y+height), (255, 0, 0), 3)

    for (x, y, width, height) in bodies:
        cv2.rectangle(frame, (x, y), (x+width, y+height), (255, 0, 0), 3)

    cv2.imshow("Cam", frame)
    # hard cascade---pre built by opencv---ML

    if cv2.waitKey(1) == ord("q"):
        break


# kills control of camera
out.release()
cap.release()
# makes sure all the windows are closed
cv2.destroyAllWindows()
