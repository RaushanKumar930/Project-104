import cv2
img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
            (90,380),
            cv2.FONT_HERSHEY_TRIPLEX,
            1,
            (100,100,255))

cv2.putText(img,
            "Mercury",
            (120,250),
            cv2.FONT_ITALIC,
            0.5,
            (200,255,200))

cv2.putText(img,
            "Venus",
            (195,260),
            cv2.FONT_ITALIC,
            0.5,
            (200,255,200))

cv2.putText(img,
            "Earth",
            (290,260),
            cv2.FONT_ITALIC,
            0.5,
            (200,255,200))

cv2.putText(img,
            "Mars",
            (390,260),
            cv2.FONT_ITALIC,
            0.5,
            (200,255,200))

cv2.putText(img,
            "Jupiter",
            (550,380),
            cv2.FONT_ITALIC,
            0.5,
            (200,255,200))

cv2.putText(img,
            "Saturn",
            (750,300),
            cv2.FONT_ITALIC,
            0.5,
            (200,255,200))

cv2.putText(img,
            "Uranus",
            (970,290),
            cv2.FONT_ITALIC,
            0.5,
            (200,255,200))

cv2.putText(img,
            "Neptune",
            (1120,285),
            cv2.FONT_ITALIC,
            0.5,
            (200,255,200))

cv2.imshow("output", img)
cv2.waitKey(0)

cv2.imwrite("Solar_system_with_name.jpg", img)