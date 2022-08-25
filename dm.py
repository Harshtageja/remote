import cv2
import os
 # set video height
faceCascade = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
# For each person, enter one numeric face id
face_id = input('\n enter user id end press <return> ==>  ')
print("\n [INFO] Initializing face capture. Look the camera and wait ...")
cap = cv2.VideoCapture(0)
# Initialize individual sampling face count
count = 0
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(img)
    print(faces)
    for (x,y,w,h) in faces:
        print("harsh")
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        count+=1
        cv2.imwrite("Harsh2/User." + str(face_id) + '.' +  
                    str(count) + ".jpg", img[y:y+h,x:x+w])
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]  
    print("harsh")
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
    elif count >=10:
        break
cap.release()
cv2.destroyAllWindows()
