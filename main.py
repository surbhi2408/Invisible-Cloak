# Importing Libraries
import cv2
import numpy as np
import time


print("""
    Hey !! Ms Surbhi Lets get deep in Image Processing be Ready to try Invisibility test.
     """)

cap = cv2.VideoCapture(0)

time.sleep(5)
c = 0  # count
background = 0

for i in range(50):  # captures the background in 50 iterations
    ret, background = cap.read()

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break
    c = c + 1

    # Converting the color space from BGR to HSV #HSV=Hue Saturation Value(Hue changes for colour but saturation and value remains same for a range)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Generating mask to detect red color
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    mask1 = mask1 + mask2  # covering background with mask

    # Refining the mask corresponding to the detected red color
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    mask1 = cv2.dilate(mask1, np.ones((3, 3), np.uint8), iterations=1)
    mask2 = cv2.bitwise_not(mask1)

    # Creating the final
    res1 = cv2.bitwise_and(background, background, mask=mask1)  # performing bitwise And
    res2 = cv2.bitwise_and(img, img, mask=mask2)
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    # imshow to see the result (magic)
    cv2.imshow('Magical !!!', final_output)
    k = cv2.waitKey(10)

    if k == ord('q'):  # press esc key to quit
        break

cap.release()
cv2.destroyAllWindows()  # Destroys all windows(quit)
