import cv2
import time
import glob
import os
from threading import Thread
from emailing import send_email


video = cv2.VideoCapture(0)
time.sleep(1)

first_frame = None
status_list = []
count = 1


def clean_folder():
    print("clean_folder function started")
    images = glob.glob("images/*.png")
    for image in images:
        os.remove(image)
    print("clean_folder function ended")

while True:
    status = 0
    check, frame = video.read()

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #converting rgb to grey
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = gray_frame_gau  #holding first_frame bcoz of differences bteween very first first frame to detect objects

    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)

    thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]  #reassigning 60 and above values to 255
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)
    cv2.imshow("My video", dil_frame)

    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  #detect contour around object

    for contour in contours:
        if cv2.contourArea(contour) < 5000:  #detecting fake object
            continue
        x, y, w, h = cv2.boundingRect(contour)  #detect obj and draw rect
        rectangle = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        if rectangle.any():
            status = 1
            cv2.imwrite(f"images/{count}.png", frame)  #to save image
            count = count + 1
            all_images = glob.glob("images/*.png")
            index = int(len(all_images) / 2)
            image_with_object = all_images[index]  #sending middle picture 



    status_list.append(status)
    status_list = status_list[-2:]

    if status_list[0] == 1 and status_list[1] == 0:  #when object is exited
        email_thread = Thread(target=send_email, args=(image_with_object, ))
        email_thread.daemon = True
        clean_thread = Thread(target=clean_folder)
        email_thread.daemon = True

        email_thread.start()



    print(status_list)

    cv2.imshow("Video", frame)
    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()

clean_thread.start()
